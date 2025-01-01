# from typing import Dict
# from typing import List


def filter_by_state(
    list_of_operations: list[dict[str, str | int]], status: str = "EXECUTED"
) -> list[dict[str, str | int]]:
    filtered_list_of_operations = []
    for i in list_of_operations:
        if i['state'] == status:
            filtered_list_of_operations.append(i)
    return filtered_list_of_operations

# test_list = [
#     {"id": 41428829, "state": "EXECUTED", "date": "2019-07-03T18:35:29.512364"},
#     {"id": 939719570, "state": "EXECUTED", "date": "2018-06-30T02:08:58.425572"},
#     {"id": 594226727, "state": "CANCELED", "date": "2018-09-12T21:27:25.241689"},
#     {"id": 615064591, "state": "CANCELED", "date": "2018-10-14T08:21:33.419441"},
# ]
# print(filter_by_state(test_list, "EXECUTED"))
# print(filter_by_state(test_list, 'CANCELED'))