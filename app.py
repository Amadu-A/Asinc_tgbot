from aiogram import executor

from loader import dp


async def on_startup(_):
    print('Бот вышел в онлайн')


if __name__ == '__main__':
    from handlers import client, admin, brute

    client.register_handlers_client(dp)
    admin.register_handlers_admin(dp)
    brute.register_handlers_other(dp)
    executor.start_polling(dp, skip_updates=True, on_startup=on_startup)
