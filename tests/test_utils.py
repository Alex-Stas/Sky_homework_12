# import pytest
from src.utils import get_transactions_from_file


# Корректный вывод utils.py после обработки тестового файла test_operations.json
utils_correct_output = [
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

def test_get_transactions_from_file_correct():
    assert get_transactions_from_file('./data/test_operations.json') == utils_correct_output

def test_get_transactions_from_file_no_file(capsys):
    result = get_transactions_from_file('./data/test_operations2.json')
    result_str = str(capsys.readouterr())
    assert result == []
    assert result_str == "CaptureResult(out='Файл не найден\\n', err='')"

def test_get_transactions_from_file_bad_format_or_empty(capsys):
    result = get_transactions_from_file('./data/test_operations_empty.json')
    result_str = str(capsys.readouterr())
    assert result == []
    assert result_str == "CaptureResult(out='Некорректный список транзакций\\n', err='')"