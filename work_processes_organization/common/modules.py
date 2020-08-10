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
            try:
                filepath = join(ExcelHandler.root_folder_schedules, filename)
                print(filepath)
                wb = openpyxl.load_workbook(filepath)
                sheet = wb.active
                return wb['Sheet1']
            except FileNotFoundError:
                print(f'Couldn\'t open "{filename}" file not found')
        else:
            files = os.listdir(src_dir)
            return [x for x in files if isfile(join(src_dir, x)) and x.endswith('.xlsx') and not x.startswith('~')]

    @staticmethod
    def export_schedule():
        pass

    @staticmethod
    def line_grab(row_num):
        if sheet.cell(row=row_num, column=1).value == 'Job':  # Headers
            line_type = 'headers'
            return line_type
        elif isinstance(sheet.cell(row=row_num, column=5).value, datetime.datetime):  # Datetime
            line_type = 'DATETIME'
            return line_type
        elif isinstance(sheet.cell(row=row_num, column=2).value, str):
            line_type = "DATA"
            return line_type
        else:
            return 'empty line'


# for line in grab_excel(filename='Installation Schedule - 2020.xlsx'):
#     print(line)
sheet = ExcelHandler.import_schedule(filename='Metal Shop Schedule - 2020.xlsx')
print(sheet)

a = ExcelHandler(123, 'asdfasdf', 'pap 03', 'vasya pupkin', out_paint=False)
print(a)
print(sheet.cell(row=1, column=2))
print(f'rows = {sheet.max_row}, columns = {sheet.max_column}')
for row in range(1, 500):  # sheet.max_row
    print(f'\n{row} -= {ExcelHandler.line_grab(row)} =-\n')
    for cell in range(1, sheet.max_column):
        cell_value = sheet.cell(row=row, column=cell).value
        if cell_value:
            if isinstance(cell_value, str) and not cell_value.startswith('='):
                print(sheet.cell(row=row, column=cell).value)


# print(f"SPECIAL REQUEST ANSWER IS {sheet['E478'].value}", f"TYPE = ", type(sheet['E478'].value))
"""
markers:
if column['E'].isinstance('datetime.datetime') /
or column['A'] is not Null /
or column

line_types:
headers
date - save only one cell
model - cell with 
summary  - ignore, dynamic data, i cant save it directly
empty - just ignore


SPECIAL REQUEST ANSWER IS 2020-08-03 00:00:00 TYPE =  <class 'datetime.datetime'>
"""
