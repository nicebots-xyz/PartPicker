# Copyright (c) NiceBots all rights reserved - refer to LICENSE file in the root

import discord
import re

from .scraper import PartPickerManager
from discord.ext import commands
from schema import Schema
from src.logging import logger


default = {
    "enabled": True,
}

schema = Schema(
    {
        "enabled": bool,
    }
)

pcpartpicker_pattern = r"https?://(?:(?:[\w-]+\.)?pcpartpicker\.com)/list/[\w-]+"


def find_pcpartpicker_links(text, unique=True) -> list[str]:
    """
    Find all PCPartPicker links in the given text.

    Args:
    text (str): The input text to search for PCPartPicker links.

    Returns:
    list: A list of all PCPartPicker links found in the text.
    """
    if unique:
        return list(set(re.findall(pcpartpicker_pattern, text)))
    return re.findall(pcpartpicker_pattern, text)


class PartPicker(commands.Cog):
    def __init__(self, bot: discord.Bot):
        self.bot = bot
        self.part_picker_manager = PartPickerManager(logger)

    @discord.Cog.listener("on_message")
    async def on_message(
        self,
        message: discord.Message,
    ):
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
                logger.error(f"Error fetching PCPartPicker list: {e}")
                continue
            embed = discord.Embed(
                title=parts_list.url,
                url=parts_list.url,
                color=discord.Color.blurple(),
            )
            embed.set_author(name="PCPartPicker")
            description = "\n".join(
                f"**{part.type}** - [{part.name}]({part.url})"
                for part in parts_list.parts
            )
            embed.description = description
            embeds.append(embed)
        await message.reply(embeds=embeds, mention_author=False)


def setup(bot: discord.Bot) -> None:
    bot._connection._intents.message_content = True
    bot.add_cog(PartPicker(bot))
