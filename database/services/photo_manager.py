from sqlalchemy import select, func

from database import Database
from database.models import Photo


class PhotoManager:
    def __init__(self) -> None:
        self._session_maker = Database().session_maker

    async def create_photo(self, file_id: str, file_unique_id: str) -> Photo | None:
        # checking for the existence of a photo
        exist_photo = await self.get_photo_by_file_unique_id(file_unique_id)
        if exist_photo is not None:
            return None

        # creating a photo
        photo = Photo(file_id=file_id, file_unique_id=file_unique_id)
        async with self._session_maker.begin() as session:
            session.add(photo)
            await session.commit()
        return photo

    async def get_photo(self, photo_id: int) -> Photo | None:
        async with self._session_maker.begin() as session:
            return await session.get(Photo, photo_id)

    async def get_photo_by_file_unique_id(self, file_unique_id: str) -> Photo | None:
        async with self._session_maker.begin() as session:
            statement = select(Photo).where(Photo.file_unique_id == file_unique_id)
            result = await session.execute(statement)
            return result.scalar_one_or_none()

    async def get_random_photo(self) -> Photo | None:
        async with self._session_maker.begin() as session:
            statement = select(Photo).order_by(func.rand()).limit(1)
            result = await session.execute(statement)
            return result.scalar_one_or_none()

    async def get_all_photos(self):
        async with self._session_maker.begin() as session:
            statement = select(Photo)
            result = await session.execute(statement)
            return result.scalars().all()
