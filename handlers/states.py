# -*- coding: utf-8 -*-
from aiogram import Router, types
from aiogram.fsm.context import FSMContext
from aiogram.fsm.state import State, StatesGroup
from services import get_exchange_rate
from aiogram.exceptions import TelegramAPIError

router = Router()

class ConversionStates(StatesGroup):
    TO_CURRENCY = State()
    AMOUNT = State()

@router.message(ConversionStates.AMOUNT)
async def amount_handler(message: types.Message, state: FSMContext):
    try:
        amount = float(message.text)
        data = await state.get_data()
        
        try:
            rate = await get_exchange_rate(data["from_currency"], data["to_currency"])
            result = amount * rate
            
            await message.answer(
                f"🔹 Результат: <b>{amount:.2f} {data['from_currency']} = "
                f"{result:.2f} {data['to_currency']}</b>\n"
                f"📊 Курс: 1 {data['from_currency']} = {rate:.4f} {data['to_currency']}",
                parse_mode="HTML"
            )
        except TelegramAPIError as e:
            await message.answer(
                f"⚠️ Ошибка получения курса валют:\n<code>{str(e)}</code>\n"
                "Попробуйте позже или используйте /convert для повторной попытки.",
                parse_mode="HTML"
            )
            
        await state.clear()
        
    except ValueError:
        await message.answer("❌ Ошибка! Введите число, например: 100 или 50.5")