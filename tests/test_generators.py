import pytest
from src.generators import card_number_generator
from src.generators import filter_by_currency
from src.generators import transaction_descriptions


# Основной список для тестирования базовых вариантов
@pytest.fixture
def test_list():
    test_list = [
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
            "id": 142264268,
            "state": "EXECUTED",
            "date": "2019-04-04T23:20:05.206878",
            "operationAmount": {"amount": "79114.93", "currency": {"name": "USD", "code": "USD"}},
            "description": "Перевод со счета на счет",
            "from": "Счет 19708645243227258542",
            "to": "Счет 75651667383060284188",
        },
        {
            "id": 873106923,
            "state": "EXECUTED",
            "date": "2019-03-23T01:09:46.296404",
            "operationAmount": {"amount": "43318.34", "currency": {"name": "руб.", "code": "RUB"}},
            "description": "Перевод со счета на счет",
            "from": "Счет 44812258784861134719",
            "to": "Счет 74489636417521191160",
        },
        {
            "id": 895315941,
            "state": "EXECUTED",
            "date": "2018-08-19T04:27:37.904916",
            "operationAmount": {"amount": "56883.54", "currency": {"name": "USD", "code": "USD"}},
            "description": "Перевод с карты на карту",
            "from": "Visa Classic 6831982476737658",
            "to": "Visa Platinum 8990922113665229",
        },
        {
            "id": 594226727,
            "state": "CANCELED",
            "date": "2018-09-12T21:27:25.241689",
            "operationAmount": {"amount": "67314.70", "currency": {"name": "руб.", "code": "RUB"}},
            "description": "Перевод организации",
            "from": "Visa Platinum 1246377376343588",
            "to": "Счет 14211924144426031657",
        },
    ]
    return test_list


# Основной список для тестирования вариантов с отсутствием ключей
@pytest.fixture
def test_list_no_keys():
    test_list_no_keys = [
        {
            "id": 939719570,
            "state": "EXECUTED",
            "date": "2018-06-30T02:08:58.425572",
            "from": "Счет 75106830613657916952",
            "to": "Счет 11776614605963066702",
        },
        {
            "id": 142264268,
            "state": "EXECUTED",
            "date": "2019-04-04T23:20:05.206878",
            "operationAmount": {"amount": "79114.93"},
            "description": "Перевод со счета на счет",
            "from": "Счет 19708645243227258542",
            "to": "Счет 75651667383060284188",
        },
        {
            "id": 873106923,
            "state": "EXECUTED",
            "date": "2019-03-23T01:09:46.296404",
            "operationAmount": {"amount": "43318.34", "currency": {"name": "руб."}},
            "from": "Счет 44812258784861134719",
            "to": "Счет 74489636417521191160",
        },
        {
            "id": 895315941,
            "state": "EXECUTED",
            "date": "2018-08-19T04:27:37.904916",
            "operationAmount": {"amount": "56883.54", "currency": {"name": "USD", "code": "USD"}},
            "description": "Перевод с карты на карту",
            "from": "Visa Classic 6831982476737658",
            "to": "Visa Platinum 8990922113665229",
        }
    ]
    return test_list_no_keys

# Тестирование функции filter_by_currency - выбор по валюте

def test_currency(test_list, currency='USD'):
    result = filter_by_currency(test_list, 'USD')
    assert next(result) == {
            "id": 939719570,
            "state": "EXECUTED",
            "date": "2018-06-30T02:08:58.425572",
            "operationAmount": {"amount": "9824.07", "currency": {"name": "USD", "code": "USD"}},
            "description": "Перевод организации",
            "from": "Счет 75106830613657916952",
            "to": "Счет 11776614605963066702",
        }
    assert next(result) == {
        "id": 142264268,
        "state": "EXECUTED",
        "date": "2019-04-04T23:20:05.206878",
        "operationAmount": {"amount": "79114.93", "currency": {"name": "USD", "code": "USD"}},
        "description": "Перевод со счета на счет",
        "from": "Счет 19708645243227258542",
        "to": "Счет 75651667383060284188",
    }
    assert next(result) == {
            "id": 895315941,
            "state": "EXECUTED",
            "date": "2018-08-19T04:27:37.904916",
            "operationAmount": {"amount": "56883.54", "currency": {"name": "USD", "code": "USD"}},
            "description": "Перевод с карты на карту",
            "from": "Visa Classic 6831982476737658",
            "to": "Visa Platinum 8990922113665229",
        }

# Тестирование функции filter_by_currency с отсутствующими ключами (транзакции должны пропускаться)

def test_currency_no_keys(test_list_no_keys, currency='USD'):
    result = filter_by_currency(test_list_no_keys, 'USD')
    assert next(result) == {
            "id": 895315941,
            "state": "EXECUTED",
            "date": "2018-08-19T04:27:37.904916",
            "operationAmount": {"amount": "56883.54", "currency": {"name": "USD", "code": "USD"}},
            "description": "Перевод с карты на карту",
            "from": "Visa Classic 6831982476737658",
            "to": "Visa Platinum 8990922113665229",
        }

# Обработка filter_by_currency конца данных

def test_currency_end_of_data(test_list, currency='USD'):
    with pytest.raises(RuntimeError) as stop_iter:
        result = filter_by_currency(test_list, 'USD')
        for _ in range(4):
            next(result)
    assert "StopIteration" in str(stop_iter.value)

# Обработка filter_by_currency пустого списка

def test_currency_empty(test_list, currency='USD'):
    with pytest.raises(RuntimeError) as stop_iter:
        result = filter_by_currency([], 'USD')
        next(result)
    assert "StopIteration" in str(stop_iter.value)

# Обработка filter_by_currency отсутствия заданной валюты в списке

def test_currency_absent(test_list, currency='EUR'):
    with pytest.raises(RuntimeError) as stop_iter:
        result = filter_by_currency([], 'EUR')
        next(result)
    assert "StopIteration" in str(stop_iter.value)

# Базовое тестирование transaction_descriptions

def test_transaction_descriptions(test_list):
    result = transaction_descriptions(test_list)
    assert next(result) == "Перевод организации"
    assert next(result) == "Перевод со счета на счет"
    assert next(result) == "Перевод со счета на счет"
    assert next(result) == "Перевод с карты на карту"
    assert next(result) == "Перевод организации"

# Тестирование функции transaction_descriptions с отсутствующими ключами (транзакции должны пропускаться)
def test_transaction_descriptions_no_keys(test_list_no_keys):
    result = transaction_descriptions(test_list_no_keys)
    assert next(result) == "Перевод со счета на счет"
    assert next(result) == "Перевод с карты на карту"

# Обработка transaction_descriptions окончания списка

def test_transaction_descriptions_end_of_data(test_list):
    with pytest.raises(RuntimeError) as stop_iter:
        result = transaction_descriptions(test_list)
        for _ in range(6):
            next(result)
    assert "StopIteration" in str(stop_iter.value)

# Обработка transaction_descriptions пустого списка
def test_transaction_descriptions_empty(test_list):
    with pytest.raises(RuntimeError) as stop_iter:
        result = transaction_descriptions([])
        next(result)
    assert "StopIteration" in str(stop_iter.value)


# Тестирование генератора card_number_generator, включая некорректно введенные данные
@pytest.mark.parametrize(
    "start, stop, expected", [
        (1, 5, ['0000 0000 0000 0001',
                '0000 0000 0000 0002',
                '0000 0000 0000 0003',
                '0000 0000 0000 0004',
                '0000 0000 0000 0005']),
        (9998, 10003, ['0000 0000 0000 9998',
                       '0000 0000 0000 9999',
                       '0000 0000 0001 0000',
                       '0000 0000 0001 0001',
                       '0000 0000 0001 0002',
                       '0000 0000 0001 0003']),
        (99999998, 100000003, ['0000 0000 9999 9998',
                               '0000 0000 9999 9999',
                               '0000 0001 0000 0000',
                               '0000 0001 0000 0001',
                               '0000 0001 0000 0002',
                               '0000 0001 0000 0003']),
        (999999999998, 100000000003, ['0000 9999 9999 9998',
                                      '0000 9999 9999 9999',
                                      '0001 0000 0000 0000',
                                      '0001 0000 0000 0001',
                                      '0001 0000 0000 0002',
                                      '0001 0000 0000 0003']),
        (9999999999999995, 9999999999999999, ['9999 9999 9999 9995',
                                              '9999 9999 9999 9996',
                                              '9999 9999 9999 9997',
                                              '9999 9999 9999 9998',
                                              '9999 9999 9999 9999']),
        (5, 1, 'Incorrect range'),
        (1.9, 2, 'Incorrect range'),
        (1, '5', 'Incorrect range'),
        (1, 12345678901234567, 'Incorrect range')
    ]
)
def card_number_generator(start, stop, expected):
    assert card_number_generator(start, stop) == expected
