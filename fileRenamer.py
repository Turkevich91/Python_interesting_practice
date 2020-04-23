import os
from pathlib import Path

path = r'P:\_Programming_JOBS\_Turret Punch_\2018\1873 Reston Office Bldg 3 & Garage\PAP 02'
print(os.listdir(path))
os.chdir(path)  # получает список файлов в папке

for f in [f for f in os.listdir(path) if f.lower().endswith('.dwg')]:
    fPath = os.path.join(path, f)
    if len(f.split('-')) == 3 and os.path.isfile(fPath):
        file_name, file_ext = os.path.splitext(f)   # Делим файл на имя и расширение
        f_job, f_release, f_num = file_name.split('-')  # Делим имя файла по метке "-" на 3 части
        newName = ('{}-{}{}'.format(f_release, f_num, file_ext))
        # print(newName)
        print(f, ' > ', newName)
        # os.rename(f, newName)

