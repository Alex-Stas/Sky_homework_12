import pandas as pd


def get_transactions_from_excel_file(file_path: str) -> list:
    """Функция принимает на вход путь до excel-файла и возвращает список словарей
     с данными о финансовых транзакциях.
    Если файл не найден, функция возвращает пустой список с сообщением об ошибке.
    Если файл пустой возвращается пустой список"""

    try:
        df = pd.read_excel(file_path)
        # replacing default 'nan' for empty cells with ""
        df_wo_nan = df.fillna("")
        transactions_list = df_wo_nan.to_dict(orient="records")
    except FileNotFoundError:
        print("Файл не найден")
        return []

    return transactions_list


# Тестовый блок, для запуска раскомментировать
# if __name__ == "__main__":
# result = get_transactions_from_excel_file("../data/transactions_excel_test.xlsx")
# if not result:
#     print(result)
# else:
#     for i in result:
#         print(i)
