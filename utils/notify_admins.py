from aiogram import Bot
from config import ADMIN_ID



async def on_startup_notify(bot: Bot):
    await bot.send_message(chat_id=ADMIN_ID, text='Бот запущен')