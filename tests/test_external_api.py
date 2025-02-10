import pytest
from unittest.mock import patch, Mock
from src.external_api import return_amount_in_rubles_current_rate


# Тестирование конвертации и вывода в случае транзакции в рублях
def test_return_amount_in_rubles_rubles():
    transaction = {
        "id": 41428829,
        "state": "EXECUTED",
        "date": "2019-07-03T18:35:29.512364",
        "operationAmount": {"amount": "8221.37", "currency": {"name": "RUB", "code": "RUB"}},
        "description": "Перевод организации",
        "from": "MasterCard 7158300734726758",
        "to": "Счет 35383033474447895560",
    }
    result = return_amount_in_rubles_current_rate(transaction)
    assert result == 8221.37


# Тестирование конвертации и вывода в случае транзакции в валюте
def test_return_amount_in_rubles_current_rate():
    mock_response = Mock()
    mock_response.status_code = 200
    mock_response.json.return_value = {
        "success": True,
        "query": {"from": "USD", "to": "RUB", "amount": 8221.37},
        "info": {"timestamp": 1738699143, "rate": 100.684512},
        "date": "2025-02-04",
        "result": 827764.626421,
    }

    with patch("requests.get", return_value=mock_response):
        transaction = {
            "id": 41428829,
            "state": "EXECUTED",
            "date": "2019-07-03T18:35:29.512364",
            "operationAmount": {"amount": "8221.37", "currency": {"name": "USD", "code": "USD"}},
            "description": "Перевод организации",
            "from": "MasterCard 7158300734726758",
            "to": "Счет 35383033474447895560",
        }
        result = return_amount_in_rubles_current_rate(transaction)
        assert result == 827764.626421


# Тестирование отсутствия корректного ответа от сайта с курсами валют
def test_return_amount_in_rubles_current_rate_bad_status():
    mock_response = Mock()
    mock_response.status_code = 100

    with patch("requests.get", return_value=mock_response):
        transaction = {
            "id": 41428829,
            "state": "EXECUTED",
            "date": "2019-07-03T18:35:29.512364",
            "operationAmount": {"amount": "8221.37", "currency": {"name": "USD", "code": "USD"}},
            "description": "Перевод организации",
            "from": "MasterCard 7158300734726758",
            "to": "Счет 35383033474447895560",
        }
        with pytest.raises(ValueError, match="Ошибка 100 при попытке получения курса валюты"):
            return_amount_in_rubles_current_rate(transaction)


# Тестирование некорректного формата транзакции на входе в функцию - отсутствия ключа кода валюты или количества
def test_return_amount_in_rubles_bad_transaction_format():
    transaction = {
        "id": 41428829,
        "state": "EXECUTED",
        "date": "2019-07-03T18:35:29.512364",
        "operationAmount": {"amount": "8221.37", "currency": {"name": "RUB", "Code": "RUB"}},
        "description": "Перевод организации",
        "from": "MasterCard 7158300734726758",
        "to": "Счет 35383033474447895560",
    }
    with pytest.raises(KeyError, match="Некорректный формат транзакции"):
        return_amount_in_rubles_current_rate(transaction)


# Тестирование ввода неизвестного кода валюты (не RUB, USD или EUR)
def test_return_amount_in_rubles_bad_currency_code():
    transaction = {
        "id": 41428829,
        "state": "EXECUTED",
        "date": "2019-07-03T18:35:29.512364",
        "operationAmount": {"amount": "8221.37", "currency": {"name": "RUB", "code": "ZZZ"}},
        "description": "Перевод организации",
        "from": "MasterCard 7158300734726758",
        "to": "Счет 35383033474447895560",
    }
    with pytest.raises(ValueError, match="Неизвестный код валюты ZZZ - конвертация невозможна"):
        return_amount_in_rubles_current_rate(transaction)
