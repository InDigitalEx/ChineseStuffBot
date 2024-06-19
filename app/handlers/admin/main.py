from aiogram import Router
from aiogram.filters import CommandStart, Command
from aiogram.types import Message

from app.filters import IsAdmin
from data import Messages
from database.services import UserManager
from .caption import caption_router
from .photo import photo_router

admin_router = Router()


@admin_router.message(CommandStart(), IsAdmin())
async def __start_admin_message(message: Message) -> None:
    user_manager = UserManager(message.from_user.id)
    user = await user_manager.create_user()

    await message.answer(Messages.START_ADMIN.format(
        full_name=message.from_user.full_name)
    )

@admin_router.message(Command('help'), IsAdmin())
async def __help_admin_message(message: Message) -> None:
    await message.answer(Messages.HELP_ADMIN)



@admin_router.startup()
async def __admin_router_startup(router: Router) -> None:
    router.include_routers(
        caption_router,
        photo_router
    )
