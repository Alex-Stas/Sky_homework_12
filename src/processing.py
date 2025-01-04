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


test_list = [
    {"id": 41428829, "state": "EXECUTED", "date": "2019-07-03T18:35:29.512364"},
    {"id": 939719570, "state": "EXECUTED", "date": "2018-06-30T02:08:58.425572"},
    {"id": 594226727, "state": "CANCELED", "date": "2018-09-12T21:27:25.241689"},
    {"id": 615064591, "state": "CANCELED", "date": "2018-10-14T08:21:33.419441"},
    ]
print(sort_by_date(test_list))

