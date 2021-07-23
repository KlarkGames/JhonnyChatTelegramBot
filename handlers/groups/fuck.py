from aiogram.dispatcher.filters import Command
from aiogram.types import Message

from loader import dp


@dp.message_handler(Command('fuck'))
async def fuck_someone(message: Message):
    await message.answer("Иди нахуй!")
    await message.delete()
