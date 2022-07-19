from aiogram import executor
from aiogram.types import Message

from loader import dp, bot


@dp.message_handler(commands=['start', 'help'])
async def command_start(message: Message):
    await bot.send_message(message.from_user.id, 'Приятного аппетита')


@dp.message_handler()
async def echo_send(message: Message):
    await message.answer(message.text)
    await message.reply(message.text)
    await bot.send_message(message.from_user.id, message.text)


if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)
