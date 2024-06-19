from aiogram import Router
from aiogram.filters import CommandStart
from aiogram.types import Message

from data import Messages
from database.services import UserManager

user_router = Router()


@user_router.message(CommandStart())
async def __start_message(message: Message) -> None:
    user_manager = UserManager(message.from_user.id)
    user = await user_manager.create_user()

    await message.answer(Messages.START.format(
        full_name=message.from_user.full_name)
    )
