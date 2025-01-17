import pytest
from src.masks import get_mask_account
from src.masks import get_mask_card_number


# Тестирование всех вариантов get_mask_card_number включая короткие номера, пустые и текстовые
@pytest.mark.parametrize(
    "card_number, expected",
    [
        (1234567812345678, "1234 56** **** 5678"),
        (10001111222233334444, "1000 11** **** 4444"),
        (12345678901234567890, "1234 56** **** 7890"),
        (1, "1 ** **** 1"),
        (12, "12 ** **** 12"),
        (123, "123 ** **** 123"),
        (1234, "1234 ** **** 1234"),
        (12345, "1234 5** **** 2345"),
        (123456, "1234 56** **** 3456"),
        ("", " ** **** "),
        ("1234567890123456", "1234 56** **** 3456"),
    ],
)
def test_get_mask_card_number(card_number, expected):
    assert get_mask_card_number(card_number) == expected


# Тестирование всех вариантов get_mask_account включая короткие номера, пустые и текстовые
@pytest.mark.parametrize(
    "full_account_number, expected",
    [
        (1234567812345678, "**5678"),
        (10001111222233334444, "**4444"),
        (12345678901234567890, "**7890"),
        (1, "**1"),
        (12, "**12"),
        (123, "**123"),
        (1234, "**1234"),
        (12345, "**2345"),
        (123456, "**3456"),
        ("", "**"),
        ("1234567890123456", "**3456"),
    ],
)
def test_get_mask_account(full_account_number, expected):
    assert get_mask_account(full_account_number) == expected
