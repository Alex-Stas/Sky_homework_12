import pytest
from src.processing import filter_by_state
from src.processing import sort_by_date


@pytest.fixture
def test_list():
    test_list = [
        {"id": 939719570, "state": "EXECUTED", "date": "2018-06-30T02:08:58.425572"},
        {"id": 594226727, "state": "CANCELED", "date": "2018-09-12T21:27:25.241689"},
        {"id": 594226728, "state": "CANCELED", "date": "2018-09-12T21:27:25.241689"},
        {"id": 615064591, "state": "CANCELED", "date": "2018-10-14T08:21:33.419441"},
        {"id": 41428829, "state": "EXECUTED", "date": "2019-07-03T18:35:29.512364"},
    ]
    return test_list


list_executed = [
    {"id": 939719570, "state": "EXECUTED", "date": "2018-06-30T02:08:58.425572"},
    {"id": 41428829, "state": "EXECUTED", "date": "2019-07-03T18:35:29.512364"},
]
list_canceled = [
    {"id": 594226727, "state": "CANCELED", "date": "2018-09-12T21:27:25.241689"},
    {"id": 594226728, "state": "CANCELED", "date": "2018-09-12T21:27:25.241689"},
    {"id": 615064591, "state": "CANCELED", "date": "2018-10-14T08:21:33.419441"},
]


@pytest.fixture
def no_state_list():
    no_state_list = [
        {"id": 41428829, "date": "2019-07-03T18:35:29.512364"},
        {"id": 939719570, "date": "2018-06-30T02:08:58.425572"},
    ]
    return no_state_list


@pytest.mark.parametrize("state, expected", [("EXECUTED", list_executed), ("CANCELED", list_canceled)])
def test_filter_by_state(test_list, state, expected):
    assert filter_by_state(test_list, state) == expected


def test_filter_by_state_empty_state(test_list):
    assert filter_by_state(test_list) == list_executed


def test_filter_by_state_no_state(no_state_list):
    with pytest.raises(KeyError):
        filter_by_state(no_state_list)


list_date_sort_descending = [
    {"id": 41428829, "state": "EXECUTED", "date": "2019-07-03T18:35:29.512364"},
    {"id": 615064591, "state": "CANCELED", "date": "2018-10-14T08:21:33.419441"},
    {"id": 594226727, "state": "CANCELED", "date": "2018-09-12T21:27:25.241689"},
    {"id": 594226728, "state": "CANCELED", "date": "2018-09-12T21:27:25.241689"},
    {"id": 939719570, "state": "EXECUTED", "date": "2018-06-30T02:08:58.425572"},
]
list_date_sort_ascending = [
    {"id": 939719570, "state": "EXECUTED", "date": "2018-06-30T02:08:58.425572"},
    {"id": 594226727, "state": "CANCELED", "date": "2018-09-12T21:27:25.241689"},
    {"id": 594226728, "state": "CANCELED", "date": "2018-09-12T21:27:25.241689"},
    {"id": 615064591, "state": "CANCELED", "date": "2018-10-14T08:21:33.419441"},
    {"id": 41428829, "state": "EXECUTED", "date": "2019-07-03T18:35:29.512364"},
]


@pytest.fixture
def list_date_sort_any_dates_string():
    list_date_sort_any_dates_string = [
        {"id": 939719570, "state": "EXECUTED", "date": "06-30-2018T02:08:58.425572"},
        {"id": 594226727, "state": "CANCELED", "date": "2018/09/12T21:27:25.241689"},
        {"id": 594226728, "state": "CANCELED", "date": "date unknown"},
        {"id": 615064591, "state": "CANCELED", "date": "2018-10-14"},
        {"id": 41428829, "state": "EXECUTED", "date": "2019-07-03T18:35:29.512364"},
    ]
    return list_date_sort_any_dates_string


list_date_sort_any_dates = [
    {"id": 594226728, "state": "CANCELED", "date": "date unknown"},
    {"id": 41428829, "state": "EXECUTED", "date": "2019-07-03T18:35:29.512364"},
    {"id": 594226727, "state": "CANCELED", "date": "2018/09/12T21:27:25.241689"},
    {"id": 615064591, "state": "CANCELED", "date": "2018-10-14"},
    {"id": 939719570, "state": "EXECUTED", "date": "06-30-2018T02:08:58.425572"},
]


@pytest.fixture
def list_date_sort_no_date():
    list_date_sort_no_date = [
        {"id": 939719570, "state": "EXECUTED", "date": "2018-06-30T02:08:58.425572"},
        {"id": 594226727, "state": "CANCELED"},
    ]
    return list_date_sort_no_date


@pytest.fixture
def list_date_sort_wrong_type():
    list_date_sort_wrong_type = [
        {"id": 939719570, "state": "EXECUTED", "date": "2018-06-30T02:08:58.425572"},
        {"id": 594226727, "state": "CANCELED", "date": 2018},
    ]
    return list_date_sort_wrong_type


@pytest.mark.parametrize(
    "descending_order, expected", [(True, list_date_sort_descending), (False, list_date_sort_ascending)]
)
def test_sort_by_date(test_list, descending_order, expected):
    assert sort_by_date(test_list, descending_order) == expected


def test_sort_by_date_empty_order(test_list):
    assert sort_by_date(test_list) == list_date_sort_descending


def test_sort_by_date_any_date_string(list_date_sort_any_dates_string):
    assert sort_by_date(list_date_sort_any_dates_string) == list_date_sort_any_dates


def test_sort_by_date_no_date(list_date_sort_no_date):
    with pytest.raises(KeyError):
        sort_by_date(list_date_sort_no_date)


def test_sort_by_date_wrong_type(list_date_sort_wrong_type):
    with pytest.raises(TypeError):
        sort_by_date(list_date_sort_wrong_type)
