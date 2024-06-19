from aiogram import Router, F
from aiogram.filters import Command
from aiogram.types import Message

from app.filters import IsAdmin
from data import Messages
from database.services import PhotoManager

photo_router = Router()


@photo_router.message(F.photo, IsAdmin())
async def __add_photo_message(message: Message) -> None:
    file_id = message.photo[-1].file_id
    file_unique_id = message.photo[-1].file_unique_id
    photo_manager = PhotoManager()
    photo = await photo_manager.create_photo(file_id, file_unique_id)

    if photo is None:
        await message.answer(Messages.ADD_PHOTO_ERROR)
    else:
        await message.answer(Messages.ADD_PHOTO.format(
            photo_id=photo.id))


@photo_router.message(Command('random_photo'), IsAdmin())
async def __random_photo_message(message: Message) -> None:
    photo_manager = PhotoManager()
    photo = await photo_manager.get_random_photo()

    if photo is None:
        await message.answer(Messages.RANDOM_PHOTO_ERROR)
    else:
        await message.answer_photo(photo.file_id,
                                   Messages.RANDOM_PHOTO.format(photo_id=photo.id))
