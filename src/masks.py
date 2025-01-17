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



# test_data = [1234567812345678, 10001111222233334444, 12345678901234567890, 1, 12, 123, 1234, 12345, 123456, '', '1234567890123456']
# results = []
# for i in test_data:
#     results.append(get_mask_card_number(i))
#     print(f'{i}| |{get_mask_card_number(i)}')
# print(results)
#
# final = []
# for j in range(len(results)):
#     final.append((test_data[j], results[j]))
# print(final)
#
#
# test_data2 = [1234567812345678, 10001111222233334444, 12345678901234567890, 1, 12, 123, 1234, 12345, 123456, '', '1234567890123456']
# results2 = []
# for i in test_data2:
#     results2.append(get_mask_account(i))
#     print(f'{i}| |{get_mask_account(i)}')
# print(results2)
#
# final2 = []
# for j in range(len(results2)):
#     final2.append((test_data2[j], results2[j]))
# print(final2)