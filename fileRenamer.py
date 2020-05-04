import os

Path = r'P:\_Programming_JOBS\_Turret Punch_\2018\1873 Reston Office Bldg 3 & Garage\PAP 11'
# print('укажите путь к папке:')
# Path = input()


def file_rename(f):
    if len(f.split('-')) == 3 and os.path.isfile(f):
        file_name, file_ext = os.path.splitext(f)  # Делим файл на имя и расширение
        f_job, f_release, f_num = file_name.split('-')  # Делим имя файла по метке "-" на 3 части
        new_name = ('{}-{}{}'.format(f_release, f_num, file_ext))
        # print(newName)
        print(f, ' > ', new_name)
        os.rename(f, new_name)  # Раскоментировать перед применением
    else:
        print('--== change is not necessary ==--')


def files_rename(path):
    print(os.listdir(path))
    os.chdir(path)  # Смена текущей директории

    for f in [f for f in os.listdir(path) if f.lower().endswith('.dwg')]:
        print(f)
        file_rename(f)


files_rename(Path)
