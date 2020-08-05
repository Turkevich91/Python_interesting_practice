import openpyxl
from openpyxl.utils import get_column_letter, column_index_from_string
import os
from os.path import isfile, join, splitext, exists

SCHEDULES_FOLDER = r"\\mcp-fsvs2\Schedules"


def import_schedule(path=SCHEDULES_FOLDER, filename=None):
    """этот модуль собирает данные с таблиц и добавляет их в базу данных.
    Если не задать аргументы метод возвращает список файлов .xlsx с папки SCHEDULES
    Если передать аргумент filename (должен соответствовать существующим файлам)
     то скопирует содержимое файла в базу данных.
    """
    if filename:
        if exists(join(path, filename)):
            print(f'You are going to open file "{filename}"')
        else:
            print(f'file "{filename}" is not exist, check file name and try again')
    else:
        files = os.listdir(path)
        return [x for x in files if isfile(join(path, x)) and x.endswith('.xlsx') and not x.startswith('~')]


def export_schedule():
    pass


# for line in grab_excel(filename='Installation Schedule - 2020.xlsx'):
#     print(line)

import_schedule(filename='Installation Schedule - 2020.xlsx')
