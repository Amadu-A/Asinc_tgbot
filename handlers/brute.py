from aiogram.types import Message
from aiogram import Dispatcher
import json
import string

from loader import dp


# @dp.message_handler()
async def echo_send(message: Message):
    if {i.lower().translate(str.maketrans('', '', string.punctuation)) for i in message.text.split(' ')}\
        .intersection(set(json.load(open('utils/cenz.json')))) != set():
        await message.reply('Маты запрещены')
        await message.delete()

def register_handlers_other(dp: Dispatcher):
    dp.register_message_handler(echo_send)
