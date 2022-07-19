from aiogram import Bot
from aiogram.types import BotCommand, BotCommandScopeDefault


async def set_default_commands(bot: Bot):
    return await bot.set_my_commands(
        commands=[
            BotCommand('command_default_1', 'Стандартная команда 1'),
            BotCommand('command_default_2', 'Стандартная команда 2'),
            BotCommand('command_default_3', 'Стандартная команда 3'),
            BotCommand('command_default_4', 'Стандартная команда 4'),
        ],
        scope=BotCommandScopeDefault()
    )