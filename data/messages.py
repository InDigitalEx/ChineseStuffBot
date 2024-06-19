from abc import ABC
from dataclasses import dataclass
from typing import Final


@dataclass(frozen=True)
class Messages(ABC):
    START: Final = ('<b>Привет, {full_name}</b>!\n\n'
                    'Тебе тут ничего не доступно')
    START_ADMIN: Final = ('<b>Привет, {full_name}</b>!\n\n'
                               'Админка активна, используй <i>/help</i> для помощи')
    ADD_CAPTION: Final = ('Подпись №{caption_id} успешно добавлена\n\n'
                          'Текст: <i>{text}</i>')
    ADD_CAPTION_HELP: Final = ('Используйте: <b>/add_caption текст</b>')
    RANDOM_CAPTION: Final = ('Подпись №{caption_id}\n\n'
                             'Текст: <i>{text}</i>')
    RANDOM_CAPTION_ERROR: Final = ('Подписи не добавлены, используйте <b>/add_caption</b>')
    ADD_PHOTO: Final = ('Фото №{photo_id} успешно добавлено')
    ADD_PHOTO_ERROR: Final = ('Ошибка, фото уже добавлено')
    RANDOM_PHOTO: Final = ('Фото №{photo_id}')
    RANDOM_PHOTO_ERROR: Final = ('Фото еще не добавлены, отправьте фото для добавления')
    HELP_ADMIN: Final = ('<b>Помощь:</b>\n\n'
                         '/add_caption текст - добавить подпись\n'
                         '/random_caption - случайная подпись\n\n'
                         'Для добавления фото - просто отправить боту фотографию\n'
                         '/random_photo - случайное фото')

