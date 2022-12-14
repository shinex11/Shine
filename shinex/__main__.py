import asyncio
import importlib

from pyrogram import idle

from shinex.modules import ALL_MODULES

loop = asyncio.get_event_loop()


async def xxx_boot():
    for all_module in ALL_MODULES:
        importlib.import_module("shinex.modules." + all_module)
    print("────────────BOT START────────────")
    await idle()
    print("GoodBye! Stopping Bot")


if __name__ == "__main__":
    loop.run_until_complete(xxx_boot())
