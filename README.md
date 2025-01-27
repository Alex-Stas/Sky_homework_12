Project: Sky_homework_12.2
Repository for Sky Pro homeworks started in December 2024

Older functions/modules are masks.py and widget.py that saved from previous homeworks.

Module Processing.py with functions:

filter_by_state - Функция фильтрует список словарей с данными по транзакциям
по статусу (ключ 'state') и выдает новый список только с заданными значениями,
по умолчанию статус EXECUTED

Example with status 'EXECUTED' or empty
[{'id': 41428829, 'state': 'EXECUTED', 'date': '2019-07-03T18:35:29.512364'},
{'id': 939719570, 'state': 'EXECUTED', 'date': '2018-06-30T02:08:58.425572'}]

Example with status 'CANCELED'
[{'id': 594226727, 'state': 'CANCELED', 'date': '2018-09-12T21:27:25.241689'},
{'id': 615064591, 'state': 'CANCELED', 'date': '2018-10-14T08:21:33.419441'}]


sort_by_date - Функция возвращает новый список словарей отсортированный
по дате транзакции (поле 'date'), по умолчанию или в случае аргумента
descending_order = True первыми выводятся новые операции.

Example with descending_order = True or empty
[{'id': 41428829, 'state': 'EXECUTED', 'date': '2019-07-03T18:35:29.512364'},
{'id': 615064591, 'state': 'CANCELED', 'date': '2018-10-14T08:21:33.419441'},
{'id': 594226727, 'state': 'CANCELED', 'date': '2018-09-12T21:27:25.241689'},
{'id': 939719570, 'state': 'EXECUTED', 'date': '2018-06-30T02:08:58.425572'}]

Module generators.py with functions:

filter_by_currency - генератор, принимает на вход список словарей, представляющих транзакции и возвращает
итератор, который поочередно выдает не меняя формата транзакции,
где валюта операции соответствует заданной (например, USD).

Пример:

usd_transactions = filter_by_currency(transactions, "USD")
for _ in range(2):
    print(next(usd_transactions))

>>> {
          "id": 939719570,
          "state": "EXECUTED",
          "date": "2018-06-30T02:08:58.425572",
          "operationAmount": {
              "amount": "9824.07",
              "currency": {
                  "name": "USD",
                  "code": "USD"
              }
          },
          "description": "Перевод организации",
          "from": "Счет 75106830613657916952",
          "to": "Счет 11776614605963066702"
      }
      {
              "id": 142264268,
              "state": "EXECUTED",
              "date": "2019-04-04T23:20:05.206878",
              "operationAmount": {
                  "amount": "79114.93",
                  "currency": {
                      "name": "USD",
                      "code": "USD"
                  }
              },
              "description": "Перевод со счета на счет",
              "from": "Счет 19708645243227258542",
              "to": "Счет 75651667383060284188"

transaction_descriptions - генератор, принимает список словарей с транзакциями и возвращает описание
каждой операции по очереди.

Пример:

descriptions = transaction_descriptions(transactions)
for _ in range(5):
    print(next(descriptions))

>>> Перевод организации
    Перевод со счета на счет
    Перевод со счета на счет
    Перевод с карты на карту
    Перевод организации

card_number_generator - генератор, выдает номера банковских карт в формате 
XXXX XXXX XXXX XXXX,  где Х — цифра номера карты, в заданном диапазоне
от 0000 0000 0000 0001 до 9999 9999 9999 9999.
Исходя из заданных начального и конечного значения диапазона.

Пример:

for card_number in card_number_generator(1, 5):
    print(card_number)

>>> 0000 0000 0000 0001
    0000 0000 0000 0002
    0000 0000 0000 0003
    0000 0000 0000 0004
    0000 0000 0000 0005

Working and pre-testing data for generators is in main module.

Installation:

1. Please be sure that Python 3.12 is installed or install it from python.org
2. Copy file main.py in the desired directory
3. Create src in that directory and copy processing.py there
4. Then you can run the main.py file as follows 'python main.py'
5. Both functions runs with testing data
6. Or you can import both function from processing.py into any python module you like 

Automatic tests are added for all modules.

processing.py:
    filter_by_state:
        Основное тестирование по базовому списку (опции EXECUTED, CANCELED и по умолчанию)
        Тестирование случая отсутствия ключа state
    sort_by_date:
        Тестирование основных случаев (по возрастанию/ убыванию и при отсутствующем аргументе)
        Тестирование случая нестандартных форматов дат строкового
        Тестирование случая отсутствия ключа date
        Тестирование случая нестандартных форматов дат не строкового типа 

masks.py:
    get_mask_account:
        Тестирование всех вариантов get_mask_card_number включая короткие номера, пустые и текстовые
    get_mask_account: 
        Тестирование всех вариантов get_mask_account включая короткие номера, пустые и текстовые

widget.py:
    mask_account_card:
        Тестирование всех вариантов mask_account_card включая короткие номера и отсутствие описания для карт
        Тестирование случая некорректных номеров счета и карт (пустые или нецифровые значения, в том числе вызванные коротким номером карты)
    get_date:
        Тестирование всех вариантов get_date включая короткие, неполные даты и ee отсутствие
        Тестирование случая критической ошибки, если тип данных не корректный (не str)

generators.py:
    filter_by_currency:
        Тестирование выбора по валюте
        Тестирование с отсутствующими ключами (транзакции должны пропускаться без ошибок)
        Обработка конца массива данных
        Обработка пустого списка
        Обработка отсутствия заданной валюты в списке
    transaction_descriptions:
        Базовое тестирование - вывод описаний операций
        Тестирование с отсутствующими ключами (транзакции должны пропускаться)
        Обработка окончания списка
        Обработка пустого списка
    card_number_generator:
        Тестирование генератора на диапазонах перехода через четвертую цифру,
        на максимальные и минимальные значения