from sqlalchemy import select, func

from database import Database
from database.models import Caption


class CaptionManager:
    def __init__(self) -> None:
        self._session_maker = Database().session_maker

    async def create_caption(self, text: str) -> Caption:
        caption = Caption(text=text)
        async with self._session_maker.begin() as session:
            session.add(caption)
            await session.commit()
        return caption

    async def get_caption(self, caption_id: int) -> Caption | None:
        async with self._session_maker.begin() as session:
            return await session.get(Caption, caption_id)

    async def get_random_caption(self) -> Caption | None:
        async with self._session_maker.begin() as session:
            statement = select(Caption).order_by(func.rand()).limit(1)
            result = await session.execute(statement)
            return result.scalar_one_or_none()

    async def get_all_captions(self):
        async with self._session_maker.begin() as session:
            statement = select(Caption)
            result = await session.execute(statement)
            return result.scalars().all()
