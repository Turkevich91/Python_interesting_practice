import openpyxl
from openpyxl.utils import get_column_letter, column_index_from_string
import os
import datetime
from os.path import isfile, join, splitext, exists


class ExcelHandler:
    root_folder_schedules = r"\\mcp-fsvs2\Schedules"

    def __init__(self, job, job_name, release, pm, pt_dwg=None, zha=None, flashing=None, coping=None,
                 splice_pate=None, blade_screen=None, perf=None, plate_panels=None, frames=None, strapping=None,
                 misc=None, est_mh=None, rel_date=None, shipped_date=None, date_dif=None, status=None, shipped_to=None,
                 remarks=None, loose_item=False, out_paint=False):
        self.job = job
        self.job_name = job_name
        self.release = release
        self.pm = pm
        self.loose_item = loose_item
        self.out_paint = out_paint
        self.pt_dwg = pt_dwg
        self.zha = zha
        self.flashing = flashing
        self.coping = coping
        self.splice_pate = splice_pate
        self.blade_screen = blade_screen
        self.perf = perf
        self.plate_panels = plate_panels
        self.frames = frames
        self.strapping = strapping
        self.misc = misc
        self.est_mh = est_mh
        self.rel_date = rel_date
        self.shipped_date = shipped_date
        self.date_dif = date_dif
        self.status = status
        self.shipped_to = shipped_to
        self.remarks = remarks

    @staticmethod
    def import_schedule(src_dir=root_folder_schedules, filename=None):
        """этот модуль собирает данные с таблиц и добавляет их в базу данных.
        Если не задать аргументы метод возвращает список файлов .xlsx с папки SCHEDULES
        Если передать аргумент filename (должен соответствовать существующим файлам)
        то скопирует содержимое файла в базу данных.
        """
        if filename:
            try:  # пробуем сопоставить строку и реальным именем файла, если файл найден то читаем все в переменную wb
                filepath = join(ExcelHandler.root_folder_schedules, filename)
                print(filepath)
                wb = openpyxl.load_workbook(filepath)
                return {wb[wb.sheetnames[0]], wb[wb.sheetnames[1]]}  # возвращаем отдельно 2 листа книги
            except FileNotFoundError:
                print(f'Couldn\'t open "{filename}" file not found')
        else:  # если не задано имя файла то возвращает список всех Эксель файлов в директории.
            files = os.listdir(src_dir)
            return [x for x in files if isfile(join(src_dir, x)) and x.endswith('.xlsx') and not x.startswith('~')]

    @staticmethod
    def export_schedule():
        pass

    @staticmethod
    def get_pro_list(sheet_job):  # as {Job_number:[title, saleman, PM]}
        sheet_job = sheet_job
        job_dict = dict()
        for i in range(2, sheet_job.max_row):
            lst = []
            for j in range(1, 5):
                lst.append(sheet_job.cell(row=i, column=j).value)
                # print(lst)
            job_dict.update({lst.pop(0): lst})
        for x in job_dict:
            print(f'{x}: {job_dict[x]}')
        return job_dict

    @staticmethod
    def parse_line(row_num):
        if sheet.cell(row=row_num, column=1).value == 'Job':  # Headers
            line_type = 'HEADERS'
            return line_type
        elif isinstance(sheet.cell(row=row_num, column=5).value, datetime.datetime):  # Datetime
            line_type = 'DATETIME'
            return line_type
        elif isinstance(sheet.cell(row=row_num, column=2).value, str):
            line_type = "DATA"
            return line_type
        elif isinstance(sheet.cell(row=row_num, column=7).value, str) \
                and sheet.cell(row=row_num, column=7).value.startswith('='):
            return 'SUMMARY LINE'
        else:
            return 'EMPTY LINE'


job_sheet, sheet = ExcelHandler.import_schedule(filename='Metal Shop Schedule - 2020.xlsx')
proj_list = ExcelHandler.get_pro_list(job_sheet)

""" 
с порядком тут какие-то проблемы, не знаю почему мне пришлось поменять местами переменные, так-что 
второй лист копируется в первую переменную, а 
первый лист во вторую переменную
"""
ExcelHandler.get_pro_list(job_sheet)
# print(sheet, job_sheet, isinstance(job_sheet, openpyxl.worksheet.worksheet.Worksheet), type(job_sheet))
#
# print(ExcelHandler.get_pro_list(job_sheet))
# print(proj_list[1572])

""" 
*****************
*** TEST AREA *** 
*****************
"""

print(f'rows = {sheet.max_row}, columns = {sheet.max_column}')
for row in range(1, 500):  # sheet.max_row
    print(f'\nLine:{row} -= {ExcelHandler.parse_line(row)} =-\n')
    for cell in range(1, sheet.max_column):
        cell_value = sheet.cell(row=row, column=cell).value
        if cell_value:
            if isinstance(cell_value, (str, int)):  # and not cell_value.startswith('=')
                if cell == 2:
                    print(proj_list[1572][0])
                else:
                    print(sheet.cell(row=row, column=cell).value)
