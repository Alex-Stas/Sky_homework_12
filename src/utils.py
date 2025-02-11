import json
import logging


logging.basicConfig(
    filename = '../logs/utils.log',
    filemode = 'w',
    format = '%(asctime)s:%(module)s:%(levelname)s:%(message)s',
    level = logging.DEBUG
)

logger = logging.getLogger()
# logger.setLevel(logging.DEBUG)
# file_handler = logging.FileHandler('../logs/utils.log')
# file_formatter = logging.Formatter('%(asctime)s:%(module)s:%(levelname)s:%(message)s')
# file_handler.setFormatter(file_formatter)
# logger.addHandler(file_handler)


def get_transactions_from_file(file_path: str) -> list:
    """Функция принимает на вход путь до JSON-файла и возвращает список словарей
    с данными о финансовых транзакциях. Если файл пустой, содержит не список или не найден,
     функция возвращает пустой список."""
    logger.info('get_transactions_from_file started')
    transactions_list = []
    try:
        with open(file_path, "r", encoding="utf-8") as transactions_list_file:
            try:
                transactions_list = json.load(transactions_list_file)
                logger.info(f'Receiving the transaction list from {file_path}')
            except json.JSONDecodeError:
                logger.error(f'The transaction list received from {file_path} is incorrect')
                print("Некорректный список транзакций")
                logger.info('get_transactions_from_file ended')
                return transactions_list

    except FileNotFoundError:
        logger.error(f'{file_path} is not found')
        print("Файл не найден")
        logger.info('get_transactions_from_file ended')
        return transactions_list

    logger.info('get_transactions_from_file ended')
    return transactions_list


# Тестовый блок, для запуска раскомментировать
if __name__ == '__main__':
    result = get_transactions_from_file('../data/test_operations_empty.json')
    print(result)
