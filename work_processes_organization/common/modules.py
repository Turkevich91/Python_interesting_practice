import openpyxl
from openpyxl.utils import get_column_letter, column_index_from_string
import os
from os.path import isfile, join, splitext, exists


class ExcelHandler:
    root_folder_schedules = r"\\mcp-fsvs2\Schedules"

    def __init__(self, job, job_name, release, pm, loose_item: False, out_paint, pt_dwg, zha, flashing, coping,
                 splice_pate, blade_screen, perf, plate_panels, frames, strapping, misc, est_mh, rel_date, shipped_date,
                 date_dif, status, shipped_to, remarks):
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


# for line in grab_excel(filename='Installation Schedule - 2020.xlsx'):
#     print(line)

print(ExcelHandler.import_schedule(filename='Metal Shop Schedule - 2020.xlsx'))
a = ExcelHandler(123, 'asdfasdf', 'pap 03', 'vasya pupkin', out_paint=False)
