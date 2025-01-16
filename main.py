from typing import Dict
from typing import List
from typing import Union

from src.processing import filter_by_state
from src.processing import sort_by_date

if __name__ == "__main__":

    # test_list: List[Dict[str, Union[str, int]]] = [
    #     {'id': 939719570, 'state': 'EXECUTED', 'date': '2018-06-30T02:08:58.425572'},
    #     {'id': 594226727, 'state': 'CANCELED', 'date': '2018-09-12T21:27:25.241689'},
    #     {'id': 594226728, 'state': 'CANCELED', 'date': '2018-09-12T21:27:25.241689'},
    #     {'id': 615064591, 'state': 'CANCELED', 'date': '2018-10-14T08:21:33.419441'},
    #     {'id': 41428829, 'state': 'EXECUTED', 'date': '2019-07-03T18:35:29.512364'}
    # ]

    test_list: List[Dict[str, Union[str, int]]] = [
        {'id': 939719570, 'state': 'EXECUTED', 'date': '06-30-2018T02:08:58.425572'},
        {'id': 594226727, 'state': 'CANCELED', 'date': '2018/09/12T21:27:25.241689'},
        {'id': 594226728, 'state': 'CANCELED', 'date': 'date unknown'},
        {'id': 615064591, 'state': 'CANCELED', 'date': '2018-10-14'},
        {'id': 41428829, 'state': 'EXECUTED', 'date': '2019-07-03T18:35:29.512364'}
    ]

    # print(filter_by_state(test_list, "EXECUTED"))
    # print(filter_by_state(test_list, "CANCELED"))
    # print(filter_by_state(test_list, ))

    # print(sort_by_date(test_list, False))
    print(sort_by_date(test_list))
