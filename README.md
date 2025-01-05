Project: Sky_homework_12.2
Repository for Sky Pro's homeworks started in December 2024

Older functions/modules are masks.py and widget.py that saved from previous homeworks.

Actual module is Processing.py with functions:

filter_by_state - Функция фильтрует список по статусу и выдает новый список только с заданными
значениями, по умолчанию статус EXECUTED

Example with status 'EXECUTED' or empty
[{'id': 41428829, 'state': 'EXECUTED', 'date': '2019-07-03T18:35:29.512364'}, {'id': 939719570, 'state': 'EXECUTED', 'date': '2018-06-30T02:08:58.425572'}]

Example with status 'CANCELED'
[{'id': 594226727, 'state': 'CANCELED', 'date': '2018-09-12T21:27:25.241689'}, {'id': 615064591, 'state': 'CANCELED', 'date': '2018-10-14T08:21:33.419441'}]


sort_by_date - Функция возвращает новый список отсортированный по дате транзакции, по умолчанию или
в случае аргумента descending_order = True первыми выводятся новые операции.

Example with descending_order = True or empty
[{'id': 41428829, 'state': 'EXECUTED', 'date': '2019-07-03T18:35:29.512364'}, {'id': 615064591, 'state': 'CANCELED', 'date': '2018-10-14T08:21:33.419441'}, {'id': 594226727, 'state': 'CANCELED', 'date': '2018-09-12T21:27:25.241689'}, {'id': 939719570, 'state': 'EXECUTED', 'date': '2018-06-30T02:08:58.425572'}]

Testing data for both functions is in main module.
