from src.widget import mask_account_card
from src.decorators import log

if __name__ == "__main__":
    pass
    # Для тестирования декоратора log - раскомментировать код ниже!
    # ********************************
    # test_data = [
    #     "Maestro 1596837868705199", "Счет 64686473678894779589","MasterCard 7158300734726758","Счет 35383033474447895560",
    #     "Visa Classic 6831982476737658","Visa Platinum 8990922113665229", "Visa Gold 5999414228426353",
    #     "Счет 73654108430135874305", "Счет 1", "Счет 1234", "Счет 12345", "Счет 123456", "1234567890123456","1234","1"
    #     ]
    #
    # for i in test_data:
    #     mask_account_card(i)
    #
    # incorrect_data = ["Счет ", "Счет A", "Visa Gold 599941422842635", "Visa Gold A99941422842635"]
    # mask_account_card(incorrect_data[1])
    # ********************************
    # конец блока кода для тестирования декоратора log
