import openpyxl
from openpyxl.utils import get_column_letter, column_index_from_string
import os
from os.path import isfile, join, splitext

SCHEDULES_FOLDER = r"\\mcp-fsvs2\Schedules"


def grab_schedule(path=SCHEDULES_FOLDER, filename=None):
    """этот модуль собирает данные с таблиц и добавляет их в базу данных.
    Без аргументов метод возвращает список файлов .xlsx с папки SCHEDULES
    Если передать аргумент filename то скопирует содержимое файла в базу данных.
    """
    if filename:
        print(f'You are going to open file {filename}')
    else:
        files = os.listdir(path)
        return [x for x in files if isfile(join(path, x)) and not x.startswith('~') and x.endswith('.xlsx')]


# for line in grab_excel(filename='Installation Schedule - 2020.xlsx'):
#     print(line)

grab_schedule(filename='Installation Schedule - 2020.xlsx')
