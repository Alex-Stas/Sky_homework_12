def get_mask_card_number(full_card_number: int) -> str:
    """
    Функция принимает на вход номер карты в виде числа и возвращает
    маску номера по правилу XXXX XX** **** XXXX
    """
    card_number_string = str(full_card_number)
    masked_card_number = f"{card_number_string[:4]} {card_number_string[4:6]}** **** {card_number_string[-4:]}"
    return masked_card_number


def get_mask_account(full_account_number: int) -> str:
    """
    Функция принимает на вход номер счета в виде числа и возвращает
    маску номера по правилу **XXXX
    """
    account_number_string = str(full_account_number)
    masked_account_number = f"**{account_number_string[-4:]}"
    return masked_account_number


if __name__ == "__main__":
    account_numbers = [
        1234567812345678,
        10001111222233334444,
        12345678901234567890,
        1,
        12,
        123,
        1234,
        12345,
        123456,
        "",
        "1234567890123456",
        None,
        True
    ]
    for i in account_numbers:
        print(get_mask_account(i))
    for i in account_numbers:
        print(get_mask_card_number(i))