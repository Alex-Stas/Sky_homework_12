from typing import Dict
from typing import List
from typing import Union


def filter_by_state(
    list_of_operations: List[Dict[str, Union[str, int]]], status: str = "EXECUTED"
) -> List[Dict[str, Union[str, int]]]:
    """Функция фильтрует список по статусу и выдает новый список только с заданными
    значениями, по умолчанию статус EXECUTED"""
    filtered_list_of_operations = []
    for i in list_of_operations:
        if "state" not in i:
            raise KeyError('One or more status keys are missing')
        #В случае отсутствия в исходных данных ключа 'state' обработка останавливается
        if i["state"] == status:
            filtered_list_of_operations.append(i)
    return filtered_list_of_operations


def sort_by_date(
    list_of_operations: List[Dict[str, Union[str, int]]], descending_order: bool = True
) -> List[Dict[str, Union[str, int]]]:
    """Функция возвращает новый список отсортированный по дате транзакции, по умолчанию или
    в случае аргумента descending_order = True первыми выводятся новые операции"""
    for i in list_of_operations:
        if "date" not in i:
            raise KeyError('One or more date keys are missing')
        if not isinstance(i['date'], str):
            raise TypeError('Date must be string')
    sorted_list_of_operations = sorted(list_of_operations, key=lambda x: x["date"], reverse=descending_order)
    return sorted_list_of_operations
