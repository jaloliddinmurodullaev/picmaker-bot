from aiogram import types
from aiogram.types import InputFile
from PIL import Image

from loader import dp
from utils import photomaker


@dp.message_handler(content_types='text')
async def bot_echo(message: types.Message):
    await photomaker(str(message.text))
    photofile = InputFile(path_or_bytesio='utils/tabrik.jpg')
    await message.reply_photo(photofile, caption="Sizning tabriknomangiz tayyor!\n@dasturchilarklubi\n@nkaunter")