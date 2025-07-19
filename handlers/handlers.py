# -*- coding: utf-8 -*
from aiogram import Router, types
from aiogram.filters import Command
from keyboards import currency_keyboard

router = Router()

@router.message(Command("start"))
async def start(message: types.Message):
    await message.answer(
        f"Привет, {message.from_user.first_name}! 👋\n"
        "Я бот для конвертации валют. Используй /convert, чтобы начать."
    )

@router.message(Command("convert"))
async def convert(message: types.Message):
    await message.answer(
        "Выбери исходную валюту:",
        reply_markup=currency_keyboard("from")  
    )


