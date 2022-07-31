from aiogram.types import Message
from aiogram import Dispatcher
from aiogram.types import ReplyKeyboardRemove

from loader import bot
from keyboards.client_kb import kb_client


# @dp.message_handler(commands=['start', 'help'])
async def command_start(message: Message):
    try:
        await bot.send_message(message.from_user.id, 'Приятного аппетита', reply_markup=kb_client)
        await message.delete()
    except:
        await message.reply("Напишите боту в лс:\nhttps://t.me/mysimple_test_bot")

# @dp.message_handler(commands=['Режим работы'])
async def open_command(message: Message):
    await bot.send_message(message.from_user.id, 'Вс-Чт с 9:00 до 20:00')

# @dp.message_handler(commands=['Расположение'])
async def place_command(message: Message):
    await bot.send_message(message.from_user.id, 'ул. Колбасная 15', reply_markup=ReplyKeyboardRemove())

def register_handlers_client(dp: Dispatcher):
    dp.register_message_handler(command_start, commands=['start', 'help'])
    dp.register_message_handler(open_command, commands=['Режим_работы'])
    dp.register_message_handler(place_command, commands=['Расположение'])

