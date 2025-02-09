# mypy: ignore-errors
import os
import requests
from dotenv import load_dotenv


def return_amount_in_rubles_current_rate(transaction):
    """
    Функция принимает на вход транзакцию и возвращает сумму транзакции (amount)
    в рублях, тип данных — float. Если транзакция была в USD или EUR
    сумма конвертируется в рубли по текущему курсу с внешнего API
    """
    if (
        "operationAmount" not in transaction
        or "currency" not in transaction["operationAmount"]
        or "code" not in transaction["operationAmount"]["currency"]
        or "amount" not in transaction["operationAmount"]
    ):
        raise KeyError("Некорректный формат транзакции")

    if transaction["operationAmount"]["currency"]["code"] == "RUB":
        return float(transaction["operationAmount"]["amount"])

    if (
        transaction["operationAmount"]["currency"]["code"] != "USD"
        and transaction["operationAmount"]["currency"]["code"] != "EUR"
    ):
        raise ValueError(
            f'Неизвестный код валюты {transaction["operationAmount"]["currency"]["code"]} - конвертация невозможна'
        )

    url = "https://api.apilayer.com/exchangerates_data/convert"

    payload = {
        "amount": transaction["operationAmount"]["amount"],
        "from": transaction["operationAmount"]["currency"]["code"],
        "to": "RUB",
    }

    load_dotenv()
    apikey = os.getenv("API_KEY")
    headers = {"apikey": apikey}

    response = requests.get(url, headers=headers, params=payload)
    # print(response.text)
    # print(response.json())
    # print(response.status_code)

    if response.status_code == 200:
        result = response.json()
        # print(result)
        amount_in_rubles = float(result["result"])
        return amount_in_rubles
    else:
        raise ValueError(f"Ошибка {response.status_code} при попытке получения курса валюты")


if __name__ == "__main__":

    transaction_list = [
        {
            "id": 441945886,
            "state": "EXECUTED",
            "date": "2019-08-26T10:50:58.294041",
            "operationAmount": {"amount": "31957.58", "currency": {"name": "руб.", "code": "RUB"}},
            "description": "Перевод организации",
            "from": "Maestro 1596837868705199",
            "to": "Счет 64686473678894779589",
        },
        {
            "id": 41428829,
            "state": "EXECUTED",
            "date": "2019-07-03T18:35:29.512364",
            "operationAmount": {"amount": "8221.37", "currency": {"name": "USD", "code": "USD"}},
            "description": "Перевод организации",
            "from": "MasterCard 7158300734726758",
            "to": "Счет 35383033474447895560",
        },
        {
            "id": 939719570,
            "state": "EXECUTED",
            "date": "2018-06-30T02:08:58.425572",
            "operationAmount": {"amount": "9824.07", "currency": {"name": "USD", "code": "USD"}},
            "description": "Перевод организации",
            "from": "Счет 75106830613657916952",
            "to": "Счет 11776614605963066702",
        },
        {
            "id": 587085106,
            "state": "EXECUTED",
            "date": "2018-03-23T10:45:06.972075",
            "operationAmount": {"amount": "48223.05", "currency": {"name": "руб.", "code": "RUB"}},
            "description": "Открытие вклада",
            "to": "Счет 41421565395219882431",
        },
        {
            "id": 142264268,
            "state": "EXECUTED",
            "date": "2019-04-04T23:20:05.206878",
            "operationAmount": {"amount": "79114.93", "currency": {"name": "USD", "code": "USD"}},
            "description": "Перевод со счета на счет",
            "from": "Счет 19708645243227258542",
            "to": "Счет 75651667383060284188",
        },
    ]

    transaction = transaction_list[0]

    result = return_amount_in_rubles_current_rate(transaction)
    print(result)
