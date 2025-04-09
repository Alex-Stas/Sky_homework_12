import csv


def get_transactions_from_csv_file(file_path: str) -> list:
    """Функция принимает на вход путь до CSV-файла (c ';' в качестве разделителя)
    и возвращает список словарей с данными о финансовых транзакциях.
    Если файл не найден, функция возвращает пустой список."""

    # transactions_list = []
    try:
        with open(file_path, "r", encoding="utf-8") as transactions_list_file:
            transactions_list = list(csv.DictReader(transactions_list_file, delimiter=";"))

    except FileNotFoundError:
        print("Файл не найден")
        return []

    return transactions_list


# Тестовый блок, для запуска раскомментировать
# if __name__ == "__main__":
#     result = get_transactions_from_csv_file("../data/transactions_test.csv")
#     if not result:
#         print(result)
#     else:
#         for i in result:
#             print(i)
