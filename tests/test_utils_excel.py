# import pytest
from src.utils_excel import get_transactions_from_excel_file

# Тестирование с помощью тестовых файлов поскольку модуль на данный момент
# не выполняет большого объема обработки и настройка тестирования корректировкой файлов
# получается гибче, чем подменой.

# Корректный вывод utils_excel.py после обработки тестового файла transactions_excel_test.xlsx
utils_excel_correct_output = [
    {
        "id": 650703.0,
        "state": "EXECUTED",
        "date": "2023-09-05T11:30:32Z",
        "amount": 16210.0,
        "currency_name": "Sol",
        "currency_code": "PEN",
        "from": "Счет 58803664561298323391",
        "to": "Счет 39745660563456619397",
        "description": "Перевод организации",
    },
    {
        "id": 3598919.0,
        "state": "EXECUTED",
        "date": "2020-12-06T23:00:58Z",
        "amount": 29740.0,
        "currency_name": "Peso",
        "currency_code": "COP",
        "from": "Discover 3172601889670065",
        "to": "Discover 0720428384694643",
        "description": "Перевод с карты на карту",
    },
    {
        "id": 593027.0,
        "state": "CANCELED",
        "date": "2023-07-22T05:02:01Z",
        "amount": 30368.0,
        "currency_name": "Shilling",
        "currency_code": "TZS",
        "from": "Visa 1959232722494097",
        "to": "Visa 6804119550473710",
        "description": "Перевод с карты на карту",
    },
    {
        "id": 366176.0,
        "state": "EXECUTED",
        "date": "2020-08-02T09:35:18Z",
        "amount": 29482.0,
        "currency_name": "Rupiah",
        "currency_code": "IDR",
        "from": "Discover 0325955596714937",
        "to": "Visa 3820488829287420",
        "description": "Перевод с карты на карту",
    },
    {
        "id": 5380041.0,
        "state": "CANCELED",
        "date": "2021-02-01T11:54:58Z",
        "amount": 23789.0,
        "currency_name": "Peso",
        "currency_code": "UYU",
        "from": "",
        "to": "Счет 23294994494356835683",
        "description": "Открытие вклада",
    },
    {
        "id": "",
        "state": "",
        "date": "",
        "amount": "",
        "currency_name": "",
        "currency_code": "",
        "from": "",
        "to": "",
        "description": "",
    },
    {
        "id": 3176764.0,
        "state": "CANCELED",
        "date": "2022-08-24T14:32:38Z",
        "amount": 16652.0,
        "currency_name": "Euro",
        "currency_code": "EUR",
        "from": "Mastercard 8387037425051294",
        "to": "American Express 5556525473658852",
        "description": "Перевод с карты на карту",
    },
    {
        "id": 4234093.0,
        "state": "EXECUTED",
        "date": "2021-07-08T07:31:21Z",
        "amount": 23182.0,
        "currency_name": "Ruble",
        "currency_code": "RUB",
        "from": "Visa 0773092093872450",
        "to": "Discover 8602781449570491",
        "description": "Перевод с карты на карту",
    },
]


# Тестирование обработки корректных данных - файл в наличии с корректной структурой
def test_get_transactions_from_file_correct():
    assert get_transactions_from_excel_file("./data/transactions_excel_test.xlsx") == utils_excel_correct_output


# Тестирование обработки отсутствия файла
def test_get_transactions_from_file_no_file(capsys):
    result = get_transactions_from_excel_file("./data/transactions_excel_test2.xlsx")
    result_str = str(capsys.readouterr())
    assert result == []
    assert result_str == "CaptureResult(out='Файл не найден\\n', err='')"


def test_get_transactions_from_empty_file():
    result = get_transactions_from_excel_file("./data/transactions_excel_empty.xlsx")
    assert result == []
