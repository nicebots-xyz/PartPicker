# Copyright (c) NiceBots all rights reserved - refer to LICENSE file in the root

import logging
import re

import discord
from discord.ext import commands
from schema import Schema

from src import custom

from .scraper import PartPickerManager

logger = logging.getLogger("bot").getChild("partpicker")


default = {
    "enabled": True,
}

schema = Schema(
    {
        "enabled": bool,
    }
)

pcpartpicker_pattern = r"https?://(?:(?:[\w-]+\.)?pcpartpicker\.com)/list/[\w-]+"


def find_pcpartpicker_links(text: str, unique: bool = True) -> list[str]:
    """Find all PCPartPicker links in the given text.

    Args:
    ----
    text (str): The input text to search for PCPartPicker links.
    unique (bool): Whether to return only unique links.

    Returns:
    -------
    list: A list of all PCPartPicker links found in the text.

    """
    if unique:
        return list(set(re.findall(pcpartpicker_pattern, text)))
    return re.findall(pcpartpicker_pattern, text)


class PartPicker(commands.Cog):
    def __init__(self, bot: discord.Bot) -> None:
        self.bot = bot
        self.part_picker_manager = PartPickerManager(logger)

    @discord.Cog.listener("on_message")
    async def on_message(
        self,
        message: discord.Message,
    ) -> None:
        if message.author.bot:
            return
        if "no-pcpp" in message.content:
            return
        embeds = []
        for url in find_pcpartpicker_links(message.content):
            if len(embeds) >= 5:
                break
            try:
                parts_list = await self.part_picker_manager.fetch_list(url)
            except Exception as e:
                logger.exception("Error fetching PCPartPicker list", exc_info=e)
                continue
            embed = discord.Embed(
                title=parts_list.url,
                url=parts_list.url,
                color=discord.Color.blurple(),
            )
            embed.set_author(name="PCPartPicker")
            description = "\n".join(f"**{part.type}** - [{part.name}]({part.url})" for part in parts_list.parts)
            embed.description = description
            embeds.append(embed)
        await message.reply(embeds=embeds, mention_author=False)


def setup(bot: custom.Bot) -> None:
    bot.intents.message_content = True
    bot.add_cog(PartPicker(bot))
