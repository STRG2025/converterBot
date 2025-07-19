from aiogram import Router, types, F
from aiogram.filters import Command, CommandObject
from aiogram.fsm.context import FSMContext
from keyboards import currency_keyboard
from handlers.states import ConversionStates

router = Router()

@router.callback_query(F.data.startswith("from_"))
async def from_currency_handler(callback: types.CallbackQuery, state: FSMContext):
    currency_from = callback.data.split("_")[1]
    await state.update_data(from_currency=currency_from)
    
    await callback.message.edit_text(
        f"Конвертируем из {currency_from}. Выбери целевую валюту:",
        reply_markup=currency_keyboard("to", exclude=currency_from)
    )
    await state.set_state(ConversionStates.TO_CURRENCY)


@router.callback_query(F.data.startswith("to_"), ConversionStates.TO_CURRENCY)
async def to_currency_handler(callback: types.CallbackQuery, state: FSMContext):
    currency_to = callback.data.split("_")[1]
    await state.update_data(to_currency=currency_to)
    
    await callback.message.edit_text(
        "Теперь введи сумму для конвертации:"
    )
    await state.set_state(ConversionStates.AMOUNT)