import json


def get_transactions_from_file(file_path: str) -> list:
    """Функция принимает на вход путь до JSON-файла и возвращает список словарей
    с данными о финансовых транзакциях. Если файл пустой, содержит не список или не найден,
     функция возвращает пустой список."""
    transactions_list = []
    try:
        with open(file_path, "r", encoding="utf-8") as transactions_list_file:
            try:
                transactions_list = json.load(transactions_list_file)
            except json.JSONDecodeError:
                print("Некорректный список транзакций")
                return transactions_list

    except FileNotFoundError:
        print("Файл не найден")
        return transactions_list

    return transactions_list


# Тестовый блок, для запуска раскомментировать
# if __name__ == '__main__':
#     result = get_transactions_from_file('../data/test_operations.json')
#     print(result)
