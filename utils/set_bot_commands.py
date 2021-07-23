from aiogram import types


async def set_default_commands(dp):
    await dp.bot.set_my_commands(
        [
            types.BotCommand("info", "Джонни расскажжет о себе"),
            types.BotCommand("fuck", "Послать нахуй"),
        ]
    )
