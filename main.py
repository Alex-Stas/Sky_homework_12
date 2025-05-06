from src.utils import get_transactions_from_file
from src.processing import filter_by_state


def main():

    greetings = """Привет!
Добро пожаловать в программу работы с банковскими транзакциями.
Выберите необходимый пункт меню:
    1. Получить информацию о транзакциях из JSON-файла
    2. Получить информацию о транзакциях из CSV-файла
    3. Получить информацию о транзакциях из XLSX-файла"""

    file_selection_data = {
        "1": "Для обработки выбран JSON-файл.",
        "2": "Для обработки выбран CSV-файл.",
        "3": "Для обработки выбран XLSX-файл.",
        "wrong selection": "Неверный выбор, повторите ввод.",
    }

    print(greetings)
    chosen_option_file = input()
    while not chosen_option_file.isnumeric():
        chosen_option_file = input(f"{file_selection_data['wrong selection']}\n")
    while chosen_option_file not in file_selection_data.keys():
        chosen_option_file = input(f"{file_selection_data['wrong selection']}\n")
    print(file_selection_data[chosen_option_file])

    status_selection_message = """Введите статус, по которому необходимо выполнить фильтрацию.
Доступные для фильтровки статусы: EXECUTED, CANCELED, PENDING"""

    status_selection_data = ["EXECUTED", "CANCELED", "PENDING"]

    print(status_selection_message)
    chosen_option_status = input().upper()
    while chosen_option_status not in status_selection_data:
        chosen_option_status = input(
            f"Статус операции {chosen_option_status} недоступен. {status_selection_message}\n"
        ).upper()
    # chosen_option_status = chosen_option_status.upper()
    print(f"Операции отфильтрованы по статусу {chosen_option_status}")

    date_sorting_message = "Отсортировать операции по дате? Да / Нет"
    date_sorting_data = ["ДА", "НЕТ"]

    print(date_sorting_message)
    chosen_option_date_sorting = input().upper()
    while chosen_option_date_sorting not in date_sorting_data:
        chosen_option_date_sorting = input("Пожалуйста, вводите только Да или Нет\n").upper()
    if chosen_option_date_sorting == "ДА":
        order_sorting_message = "Отсортировать по возрастанию или по убыванию? по возрастанию/по убыванию"
        order_sorting_data = ["ПО ВОЗРАСТАНИЮ", "ПО УБЫВАНИЮ"]

        print(order_sorting_message)
        chosen_option_order_sorting = input().upper()
        while chosen_option_order_sorting not in order_sorting_data:
            chosen_option_order_sorting = input("Пожалуйста, вводите только по возрастанию или по убыванию\n").upper()
        chosen_option_order_sorting = chosen_option_order_sorting == order_sorting_data[1]

    rouble_filter_message = "Выводить только рублевые транзакции? Да / Нет"
    rouble_filter_data = ["ДА", "НЕТ"]

    print(rouble_filter_message)
    chosen_option_rouble_filter = input().upper()
    while chosen_option_rouble_filter not in rouble_filter_data:
        chosen_option_rouble_filter = input("Пожалуйста, вводите только Да или Нет\n").upper()

    word_filter_message = "Отфильтровать список транзакций по определенному слову в описании? Да / Нет"
    word_filter_data = ["ДА", "НЕТ"]

    print(word_filter_message)
    chosen_option_word_filter = input().upper()
    while chosen_option_word_filter not in word_filter_data:
        chosen_option_word_filter = input("Пожалуйста, вводите только Да или Нет\n").upper()

    if chosen_option_word_filter == "ДА":
        word_filter = input("Введите слово для фильтра в описании\n")

    print(
        chosen_option_file,
        chosen_option_status,
        chosen_option_date_sorting,
        chosen_option_order_sorting,
        chosen_option_rouble_filter,
        chosen_option_word_filter,
        word_filter,
    )
    # match chosen_option_file:
    #     case '1':
    #         transactions = get_transactions_from_file('.\data\operations.json')
    #         transactions_filtered_by_status = filter_by_state(transactions,chosen_option_status)
    #
    #     case '2':
    #         print(2)
    #     case '3':
    #         print(3)


if __name__ == "__main__":
    main()
