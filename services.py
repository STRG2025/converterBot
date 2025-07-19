import requests
from aiogram.exceptions import TelegramAPIError
from datetime import datetime, timedelta

RATES_CACHE = {
    "data": None,
    "timestamp": None,
    "expiry": timedelta(hours=1)
}

async def get_exchange_rate(from_currency: str, to_currency: str) -> float:
    try:
        # Проверяем актуальность кэша
        if (RATES_CACHE["data"] and 
            RATES_CACHE["timestamp"] and 
            datetime.now() - RATES_CACHE["timestamp"] < RATES_CACHE["expiry"]):
            return RATES_CACHE["data"][to_currency]
        
        # Делаем запрос к API
        response = requests.get(
            f"https://api.frankfurter.app/latest?from={from_currency}",
            timeout=5  # Таймаут 5 секунд
        )
        response.raise_for_status()  # Проверяем на ошибки HTTP
        
        data = response.json()
        
        # Обновляем кэш
        RATES_CACHE["data"] = data["rates"]
        RATES_CACHE["timestamp"] = datetime.now()
        
        return data["rates"][to_currency]
        
    except requests.exceptions.RequestException as e:
        raise TelegramAPIError(f"Ошибка API: {str(e)}")
    except KeyError:
        raise TelegramAPIError("Неверный формат ответа от API")
    except Exception as e:
        raise TelegramAPIError(f"Неизвестная ошибка: {str(e)}")
