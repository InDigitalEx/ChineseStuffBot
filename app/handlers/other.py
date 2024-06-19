import logging

from aiogram import Router, Bot
from apscheduler.schedulers.asyncio import AsyncIOScheduler

from data import config
from database.services import CaptionManager, PhotoManager

other_router = Router()
scheduler = AsyncIOScheduler()


async def __send_message_to_channel(bot: Bot) -> None:
    caption_manager = CaptionManager()
    photo_manager = PhotoManager()

    caption = await caption_manager.get_random_caption()
    photo = await photo_manager.get_random_photo()

    if caption is None or photo is None:
        logging.warning('Database is empty, nothing to send')
    else:
        await bot.send_photo(
            chat_id=config.channel_name,
            photo=photo.file_id,
            caption=caption.text
        )
        logging.info('Message sent')


@other_router.startup()
async def __other_router_startup(router: Router, bot: Bot) -> None:
    scheduler.add_job(
        __send_message_to_channel,
        'interval',
        seconds=config.post_interval,
        args=(bot,)
    )
    scheduler.start()
