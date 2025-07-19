from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup

CURRENCIES = ["USD", "EUR", "RUB", "GBP", "JPY", "CNY"]

def currency_keyboard(prefix: str, exclude: str = None):
    buttons = []
    for currency in CURRENCIES:
        if currency != exclude:
            buttons.append(InlineKeyboardButton(
                text=currency,
                callback_data=f"{prefix}_{currency}"  
            ))
    return InlineKeyboardMarkup(inline_keyboard=[buttons[i:i + 3] for i in range(0, len(buttons), 3)])