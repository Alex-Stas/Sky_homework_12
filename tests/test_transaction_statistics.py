import pytest
from src.transaction_statistics import transaction_statistics_by_field


# Основной список для тестирования базовых вариантов
@pytest.fixture
def test_list():
    test_list = [
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
    return test_list


# Эталонный список статистики по полю description и по умолчанию
list_description = {"Перевод организации": 1, "Перевод с карты на карту": 5, "Открытие вклада": 1, "": 1}

# Эталонный список по полю "state"
list_state = {"EXECUTED": 4, "CANCELED": 3, "": 1}


# Список c некорректным форматом
@pytest.fixture
def list_wrong():
    list_wrong = [23, 24]
    return list_wrong


# Тестирование основных случаев transaction_statistics_by_field
@pytest.mark.parametrize(
    "field, expected",
    [("description", list_description), ("state", list_state)],
)
def test_transaction_statistics_by_field(test_list, field, expected):
    assert transaction_statistics_by_field(test_list, field) == expected


# Тестирование случая отсутствия аргумента field, default - значение
def test_transaction_statistics_by_field_default(test_list):
    assert transaction_statistics_by_field(test_list) == list_description


# Тестирование случая отсутствия ключей для поиска
def test_transaction_statistics_by_field_no_field(test_list):
    assert transaction_statistics_by_field(test_list, "descr") == {}


def test_filter_transaction_by_word_wrong_format(list_wrong):
    assert transaction_statistics_by_field(list_wrong) == {}
