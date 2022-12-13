from aiogram import types

from loader import dp
from utils import urlmaker


@dp.message_handler(content_types='text')
async def bot_echo(message: types.Message):
    await message.answer('Kutib turing...')
    await message.reply_document(document=await urlmaker("Yangi yilingiz bilan " + str(message.text)),
                                 caption='Rasm tayyor!')
