from aiogram import executor
from aiogram.types import Message

from loader import dp, bot


async def on_startup(_):
    print('Бот вышел в онлайн')


@dp.message_handler(commands=['start', 'help'])
async def command_start(message: Message):
    try:
        await bot.send_message(message.from_user.id, 'Приятного аппетита')
        await message.delete()
    except:
        await message.reply("Напишите боту в лс: \nhttps://t.me/mysimple_test_bot")

@dp.message_handler(commands=['Режим работы'])
async def open_command(message: Message):
    await bot.send_message(message.from_user.id, 'Вс-Чт с 9:00 до 20:00')

@dp.message_handler(commands=['Расположение'])
async def open_command(message: Message):
    await bot.send_message(message.from_user.id, 'ул. Колбасная 15')


@dp.message_handler()
async def echo_send(message: Message):
    if message.text == 'Привет':
        await message.answer('И тебе привет!')
    # await message.answer(message.text)
    # await message.reply(message.text)
    # await bot.send_message(message.from_user.id, message.text)


if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True, on_startup=on_startup)
