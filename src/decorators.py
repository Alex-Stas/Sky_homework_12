# mypy: ignore-errors
import time

"""
Функция - декоратор, фиксирует время начала, конца работы функции и результат её работы в случае корректного завершения;
в случае ошибки выводит сообщение об ошибке, наименование и входные данные.
Вывод в файл, если его имя дано в качестве аргумента или в консоль при его отсутствии.
    
"""
def function_log(filename='log//function_log.txt'):
    def decorator(func):
        def wrapper(*args, **kwargs):
            start_time = time.time()
            try:
                result = func(*args, **kwargs)
                finish_time = time.time()
                functon_log = f"Functon {func.__name__} started at {start_time:.2f} finished at {finish_time:.2f} its output: {result}"
                if filename:
                    with open(filename, 'a', encoding="utf-8") as file:
                        file.write(functon_log + '\n')
                else:
                    print(functon_log)
                return result
            except Exception as error:
                finish_time = time.time()
                log_message = f"Functon {func.__name__} stops with error: {str(error)}. Input data: {args}, {kwargs}"
                if filename:
                    with open(filename, 'a', encoding="utf-8") as file:
                        file.write(log_message + '\n')
                else:
                    print(log_message)
                raise error
        return wrapper
    return decorator
