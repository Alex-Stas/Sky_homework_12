from src.masks import get_mask_account
from src.masks import get_mask_card_number


def mask_account_card(account_card_description: str) -> str:
    """Определяет вариант введенного номерав карта или счет, вызывает соответствующую функцию маскировки
    и возвращает строку с замаскированным номером"""

    if account_card_description[:5] == "Счет ":
        masked_account_card = "Счет " + get_mask_account(int(account_card_description[5:]))
        return masked_account_card
    else:
        masked_account_card = account_card_description[:-16:] + get_mask_card_number(
            int(account_card_description[-16:])
        )
        return masked_account_card


def get_date(long_date: str) -> str:
    """Из строки с полной датой и временем, выделяет и возвращает дату в формате DD.MM.YYYY"""
    return f"{long_date[8:10]}.{long_date[5:7]}.{long_date[:4]}"
