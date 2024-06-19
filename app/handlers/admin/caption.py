from aiogram import Router
from aiogram.filters import Command, CommandObject
from aiogram.types import Message

from app.filters import IsAdmin
from data import Messages
from database.services import CaptionManager

caption_router = Router()


@caption_router.message(Command('add_caption'), IsAdmin())
async def __add_caption_message(message: Message, command: CommandObject) -> None:
    if command.args is None:
        await message.answer(Messages.ADD_CAPTION_HELP)
        return None

    caption_manager = CaptionManager()
    caption = await caption_manager.create_caption(command.args)
    await message.answer(Messages.ADD_CAPTION.format(
        caption_id=caption.id, text=caption.text))


@caption_router.message(Command('random_caption'), IsAdmin())
async def __random_caption_message(message: Message) -> None:
    caption_manager = CaptionManager()
    caption = await caption_manager.get_random_caption()

    if caption is None:
        await message.answer(Messages.RANDOM_CAPTION_ERROR)
    else:
        await message.answer(Messages.RANDOM_CAPTION.format(
            caption_id=caption.id, text=caption.text))
