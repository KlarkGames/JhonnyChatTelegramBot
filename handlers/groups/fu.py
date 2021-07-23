import random

from aiogram.dispatcher.filters import Command
from aiogram.types import Message

from loader import dp


@dp.message_handler(Command("fu"))
async def fu(message: Message):
    words = [
        "Алкоголь",
        "Деньги",
        "Работа",
        "Политика",
        "Курить",
        "Учиться",
        "C++",
        "Python",
        "Прогать",
        "Секс",
        "Парни",
        "Девушки",
        "Телефон",
        "Интернет",
        "Котики",
        "Собачки",
        "Адаптеры",
        "Java",
        "Kotlin",
        "Дождь",
        "Политех",
        "ИТМО",
        "Погода",
        "Дота",
        "Сериалы",
        "Книги",
        "Фильмы",
        "Порно",
        "Профсоюз",
    ]

    await message.answer(f"{random.choice(words)} фу!")
    await message.delete()