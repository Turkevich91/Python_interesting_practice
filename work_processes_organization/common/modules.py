import openpyxl
from openpyxl.utils import get_column_letter, column_index_from_string
import os
from os.path import isfile, join, splitext, exists


class ExcelHandler:
    ROOT_FOLDER_SCHEDULES = r"\\mcp-fsvs2\Schedules"

    @staticmethod
    def import_schedule(src_dir=ROOT_FOLDER_SCHEDULES, filename=None):
        """этот модуль собирает данные с таблиц и добавляет их в базу данных.
        Если не задать аргументы метод возвращает список файлов .xlsx с папки SCHEDULES
        Если передать аргумент filename (должен соответствовать существующим файлам)
         то скопирует содержимое файла в базу данных.
        """
        if filename:
            if exists(join(src_dir, filename)):
                print(f'You are going to open file "{filename}"')
            else:
                print(f'file "{filename}" is not exist, check file name and try again')
        else:
            files = os.listdir(src_dir)
            return [x for x in files if isfile(join(src_dir, x)) and x.endswith('.xlsx') and not x.startswith('~')]

    @staticmethod
    def export_schedule():
        pass


# for line in grab_excel(filename='Installation Schedule - 2020.xlsx'):
#     print(line)

print(ExcelHandler.import_schedule())
