def filter_by_state(
    list_of_operations: list[dict[str, str | int]], status: str = "EXECUTED"
) -> list[dict[str, str | int]]:
    """Функция фильтрует список по статусу и выдает новый список только с заданными
    значениями, по умолчаню статус EXECUTED"""
    filtered_list_of_operations = []
    for i in list_of_operations:
        if i["state"] == status:
            filtered_list_of_operations.append(i)
    return filtered_list_of_operations


def sort_by_date(
    list_of_operations: list[dict[str, str | int]], descending_order: bool = True
) -> list[dict[str, str | int]]:
    sorted_list_of_operations = sorted(list_of_operations, key=lambda x: x['date'], reverse=descending_order)
    return sorted_list_of_operations
