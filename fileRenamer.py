import os

Path = r'P:\_Programming_JOBS\_Turret Punch_\2019\19021_THE WORKS\PAP 04'
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


dictionary = dict()


# def rel_dictionary():  # collect all names of release folders
#     path = r"D:\Users\Public\Downloads\01ProjectEmptyFiles".upper()
#     rel_dict = set()
#     files_dict = set()
#     for year in os.listdir(path):
#         if os.path.isdir(os.path.join(path, year)):
#             for job in os.listdir(os.path.join(path, year)):
#                 if os.path.isdir(os.path.join(path, year, job)):
#                     for folder in os.listdir(os.path.join(path, year, job)):
#                         if os.path.isdir(os.path.join(path, year, job, folder)) and folder in ['ID', 'IDs', 'PD', 'PDs']:
#                             for rel in os.listdir(os.path.join(path, year, job, folder)):
#                                 if rel.count('.'):
#                                     files_dict.add(rel.upper())
#                                 else:
#                                     rel_dict.add(rel.upper())
#     for i in rel_dict:
#         print(i)
#     for i in files_dict:
#         print(i)
#     print(len(rel_dict), len(files_dict))
#
#
# rel_dictionary()


# files_rename(Path)


def get_result(path, nested_count, in_folders, result=None):
    # Если первое вхождение создаём для заполнения
    if not result:
        result = {'files': dict(), 'rel': dict()}

    # Если последняя вложенность заполняем
    if nested_count == 0:
        for rel in os.listdir(path):
            rel_path = os.path.join(path, rel)
            if os.path.isfile(rel_path):
                result['files'].update({'file': rel, 'path': rel_path})
            else:
                result['rel'].update({'folder': rel, 'path': rel_path})
        return None

    # Если не последняя вложенность бежим по папкам
    if not os.path.isdir(path):
        return None
    for folder in os.listdir(path):
        target_path = os.path.join(path, folder)
        if os.path.isdir(target_path):
            # Если не предпоследняя вложенность бежим дальше
            # В ином случае проверяем вхождение папок
            if nested_count != 1 or (folder in in_folders):
                get_result(target_path, nested_count - 1, in_folders, result)

    return result


path = r"D:\Users\Public\Downloads\01ProjectEmptyFiles"
SeekInFolders = ['ID', 'IDs', 'PD', 'PDs']
result = get_result(path, 3, SeekInFolders)
if result:
    print('files:', result['files'])
    print('rel:', result['rel'])
    print('files count:', len(result['files']), 'rel count:', len(result['rel']))
else:
    print('None to print')
