from aiogram.dispatcher.filters.builtin import Command
from aiogram.types import Message

from loader import dp


@dp.message_handler(Command('info'))
async def bot_info(message: Message):
    await message.answer(
        f"Привет, я Джон!\n"
        f"Пока я ничего не умею, во всём виноват @KlarkAl\n"
        f"Если вы хотите, чтобы я чему-то научился - обращайтесь к нему"
    )
