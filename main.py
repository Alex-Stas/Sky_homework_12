# mypy: ignore-errors

from src.utils import get_transactions_from_file
from src.utils_csv import get_transactions_from_csv_file
from src.utils_excel import get_transactions_from_excel_file
from src.transaction_filters import filter_transaction_by_word


def select_file():
    """Функция выдает приветствие и предлагает выбрать из какого файла загрузить
    возвращаемый список транзакций, далее вызывает соответствующую функцию"""

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

    match chosen_option_file:
        case "1":
            transactions_list = get_transactions_from_file(r".\data\operations.json")
        case "2":
            transactions_list = get_transactions_from_csv_file(r".\data\transactions.csv")
        case "3":
            transactions_list = get_transactions_from_excel_file(r".\data\transactions_excel.xlsx")

    return transactions_list


def status_selection(transactions_list):
    """Функция выдает сообщение и предлагает выбрать статус для фильтрации
    возвращаемого списка транзакций"""
    status_selection_message = """Введите статус, по которому необходимо выполнить фильтрацию.
Доступные для фильтровки статусы: EXECUTED, CANCELED, PENDING"""

    status_selection_data = ["EXECUTED", "CANCELED", "PENDING"]

    print(status_selection_message)
    chosen_option_status = input().upper()
    while chosen_option_status not in status_selection_data:
        chosen_option_status = input(
            f"Статус операции {chosen_option_status} недоступен. {status_selection_message}\n"
        ).upper()
    print(f"Операции отфильтрованы по статусу {chosen_option_status}")

    transactions_list_filtered_by_state = filter_transaction_by_word(transactions_list, chosen_option_status, "state")
    return transactions_list_filtered_by_state


def date_sorting(transaction_list):
    """Функция выдает сообщение сортировать ли список по датам, если да, то уточняет
    по возрастанию или убыванию и возвращает отсортированный список, если нет,
    то список возвращается без изменений"""
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

        sorted_list_of_transactions = sorted(
            transaction_list, key=lambda x: x["date"], reverse=chosen_option_order_sorting
        )
        return sorted_list_of_transactions
    else:
        return transaction_list


def rouble_filter(transaction_list):
    """Функция выдает сообщение выводить ли только рублевые транзакции из списка,
    если да, то вызывает программу фильтр и возвращает отфильтрованный список, если нет,
       то список возвращается без изменений"""

    rouble_filter_message = "Выводить только рублевые транзакции? Да / Нет"
    rouble_filter_data = ["ДА", "НЕТ"]

    print(rouble_filter_message)
    chosen_option_rouble_filter = input().upper()
    while chosen_option_rouble_filter not in rouble_filter_data:
        chosen_option_rouble_filter = input("Пожалуйста, вводите только Да или Нет\n").upper()
    if chosen_option_rouble_filter == "ДА":
        rouble_filtered_list = filter_transaction_by_word(transaction_list, "RUB", "currency_code")
        return rouble_filtered_list
    else:
        return transaction_list


def word_filter(transaction_list):
    """Функция выдает сообщение фильтровать ли транзакции из списка, по определенному слову
    если да, то запрашивает строку для фильтрации вызывает программу фильтр и
    возвращает отфильтрованный список, если нет, то список возвращается без изменений"""

    word_filter_message = "Отфильтровать список транзакций по определенному слову в описании? Да / Нет"
    word_filter_data = ["ДА", "НЕТ"]

    print(word_filter_message)
    chosen_option_word_filter = input().upper()
    while chosen_option_word_filter not in word_filter_data:
        chosen_option_word_filter = input("Пожалуйста, вводите только Да или Нет\n").upper()

    if chosen_option_word_filter == "ДА":
        word = input("Введите слово для фильтра в описании\n")
        rouble_filtered_list = filter_transaction_by_word(transaction_list, word)
        return rouble_filtered_list
    else:
        return transaction_list


def output_print(transaction_list):
    """Функция выдает выбранные на предыдущих этапах транзакции по определенному формату
    с преобразованием даты и сообщением, если список пустой"""
    if transaction_list == []:
        print("Не найдено ни одной транзакции, подходящей под ваши условия фильтрации")
        return
    print("Распечатываю итоговый список транзакций...\n")
    print(f"Всего в банковских операций в выводе: {len(transaction_list)}")

    for i in transaction_list:
        print(f"\n{i['date'][8:10]}.{i['date'][5:7]}.{i['date'][:4]} {i['description']}")
        # С учетом отсутствия значения поля 'from' для части транзакций
        try:
            if i["from"] == "":
                print(f"{i['to']}")
            else:
                print(f"{i['from']} -> {i['to']}")
        except KeyError:
            print(f"{i['to']}")
        # С учетом другого формата суммы в случае загрузки из JSON-файла
        try:
            print(f"Сумма: {i['amount']} {i['currency_name']}")
        except KeyError:
            print(f"Сумма: {i['operationAmount']['amount']} {i['operationAmount']['currency']['name']}")
    return


def main():
    """Функция последовательно запускает функции запросов и обработки списка транзакций"""
    transaction_list = select_file()
    transactions_list_filtered_by_state = status_selection(transaction_list)
    transactions_list_sorted_by_date = date_sorting(transactions_list_filtered_by_state)
    transactions_list_filtered_by_rouble = rouble_filter(transactions_list_sorted_by_date)
    transactions_list_filtered_by_word = word_filter(transactions_list_filtered_by_rouble)
    output_print(transactions_list_filtered_by_word)


if __name__ == "__main__":
    main()
