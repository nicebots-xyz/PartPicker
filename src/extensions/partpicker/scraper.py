# Copyright (c) NiceBots all rights reserved - refer to LICENSE file in the root

import logging
from pypartpicker import Scraper
from pypartpicker.scraper import PCPPList
from aiocache import SimpleMemoryCache
from aiolimiter import AsyncLimiter


class PartPickerManager:
    def __init__(self, logger: logging.Logger):
        self.scraper = Scraper()
        self.cache = SimpleMemoryCache()
        self.logger = logger
        self.large_rate_limit = AsyncLimiter(6, 60)
        self.base_rate_limit = AsyncLimiter(1, 5)

    async def fetch_list(self, list_url: str, nocache: bool = False) -> PCPPList:
        if not nocache and (parts_list := await self.cache.get(list_url)):
            self.logger.info(f"Retrieved PCPartPicker list from cache: {list_url}")
            return parts_list
        async with self.large_rate_limit:
            async with self.base_rate_limit:
                self.logger.info(f"Fetching PCPartPicker list: {list_url}")
                parts_list = await self.scraper.aio_fetch_list(list_url)
        await self.cache.set(list_url, parts_list, ttl=60 * 60)  # Cache for 1 hour
        return parts_list
