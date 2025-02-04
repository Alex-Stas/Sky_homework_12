# import pytest
from src.decorators import log

# Сообщения, которые должны выводится в консоль и файл при правильной работе декоратора с тестовой функцией
func_cons_correct = "CaptureResult(out='Functon func_cons started at finished at its output: 1.0\\n', err='')"
func_file_correct = "Functon func_file started at finished at its output: 1.0"


# Тестовая функция, декоратор log настроен на вывод в файл
@log(filename="log//function_test_log.txt")
def func_file(x, y):
    return x / y


# Тестовая функция, декоратор log настроен на вывод в консоль
@log()
def func_cons(x, y):
    return x / y


# Тестирование декоратора при корректном завершении функции и выводом в консоль
def test_func_cons_correct(capsys):
    func_cons(2, 2)
    result_str = str(capsys.readouterr())
    result_to_check = f"{result_str[:47]}{result_str[61:73]}{result_str[87:]}"
    assert result_to_check == func_cons_correct


# Тестирование декоратора при корректном завершении функции и выводом в файл
def test_func_file_correct():
    with open("log//function_test_log.txt", "w"):
        pass
    func_file(2, 2)
    with open("log//function_test_log.txt", "r") as file:
        result_str = file.readline().rstrip("\n")
    result_to_check = f"{result_str[:28]}{result_str[42:54]}{result_str[68:]}"
    assert result_to_check == func_file_correct


# Тестирование декоратора при некорректном завершении функции (деление на ноль) и выводом в консоль
def test_func_cons_error(capsys):
    try:
        func_cons(2, 0)
    except ZeroDivisionError:
        pass
    result_str = str(capsys.readouterr())
    result_to_check = (
        "CaptureResult(out='Functon func_cons stops with error: division by zero. Input data: (2, 0), {}\\n', err='')"
    )
    assert result_str == result_to_check


# Тестирование декоратора при некорректном завершении функции (деление на ноль) и выводом в файл
def test_func_file_error():
    with open("log//function_test_log.txt", "w"):
        pass
    try:
        func_file(2, 0)
    except ZeroDivisionError:
        pass
    with open("log//function_test_log.txt", "r") as file:
        result_str = file.readline().rstrip("\n")
    result_to_check = "Functon func_file stops with error: division by zero. Input data: (2, 0), {}"
    assert result_str == result_to_check
