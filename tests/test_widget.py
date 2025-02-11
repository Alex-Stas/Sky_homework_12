import pytest
from src.widget import get_date
from src.widget import mask_account_card


# Тестирование всех вариантов mask_account_card включая короткие номера и отсутствие описания для карт
@pytest.mark.parametrize(
    "account_card_description, expected",
    [
        ("Maestro 1596837868705199", "Maestro 1596 83** **** 5199"),
        ("Счет 64686473678894779589", "Счет **9589"),
        ("MasterCard 7158300734726758", "MasterCard 7158 30** **** 6758"),
        ("Счет 35383033474447895560", "Счет **5560"),
        ("Visa Classic 6831982476737658", "Visa Classic 6831 98** **** 7658"),
        ("Visa Platinum 8990922113665229", "Visa Platinum 8990 92** **** 5229"),
        ("Visa Gold 5999414228426353", "Visa Gold 5999 41** **** 6353"),
        ("Счет 73654108430135874305", "Счет **4305"),
        ("Счет 1", "Счет **1"),
        ("Счет 1234", "Счет **1234"),
        ("Счет 12345", "Счет **2345"),
        ("Счет 123456", "Счет **3456"),
        ("1234567890123456", "1234 56** **** 3456"),
        ("1234", "1234 ** **** 1234"),
        ("1", "1 ** **** 1"),
    ],
)
def test_get_mask_account_card(account_card_description, expected):
    assert mask_account_card(account_card_description) == expected


@pytest.fixture
def account_card_description_exception_list():
    account_card_description_exception_list = [
        "Счет ",
        "Счет A",
        "Visa Gold 599941422842635",
        "Visa Gold A99941422842635",
    ]
    return account_card_description_exception_list


# Тестирование случая некорректных номеров счета и карт (пустые или нецифровые значения,
# в том числе вызванные коротким номером карты)


def test_mask_account_card_exceptions(account_card_description_exception_list):
    for i in account_card_description_exception_list:
        with pytest.raises(ValueError):
            mask_account_card(i)


# Тестирование всех вариантов get_date включая короткие, неполные даты и ee отсутствие
@pytest.mark.parametrize(
    "long_date, expected",
    [
        ("2024-03-11T02:26:18.671407", "11.03.2024"),
        ("2024/03/11T02:26:18.671407", "11.03.2024"),
        ("2024-03-11", "11.03.2024"),
        ("2024", "..2024"),
        ("2024-10", ".10.2024"),
        ("", ".."),
    ],
)
def test_get_date(long_date, expected):
    assert get_date(long_date) == expected


# Тестирование случая критической ошибки, если тип данных не корректный (не str)


@pytest.fixture
def get_date_exception_list():
    get_date_exception_list = [
        20241003,
        True,
        None,
    ]
    return get_date_exception_list


def test_get_date_exception(get_date_exception_list):
    for i in get_date_exception_list:
        with pytest.raises(TypeError):
            get_date(i)
