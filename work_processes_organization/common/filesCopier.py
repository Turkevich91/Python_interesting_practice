from os import chdir, listdir, getcwd, rename
from os.path import join, isdir, splitext, basename
from shutil import copytree, copyfile
from sys import stdout
from time import sleep
import re


def files_transfer(src=None, dest=None, excel_src=None, **kwargs):
    if not src:
        src = dwgFolderApPath
    if not dest:
        dest = workFolderApPath
    if not excel_src:
        excel_src = excelPath
    try:
        copytree(src, dest, **kwargs)
        copyfile(excel_src, join(dest, 'PDF', basename(excel_src)))
    except FileExistsError:
        print('\nFiles exist overwrite them?')
        choice_request(files_transfer, dirs_exist_ok=True)


def file_rename(original_name, write=True):
    if len(original_name.split('-')) == 3:  # and os.path.isfile(file_name)
        file_name, file_ext = splitext(original_name)  # Делим файл на имя и расширение
        f_job, f_release, f_num = file_name.split('-')  # Делим имя файла по метке "-" на 3 части
        new_name = ('{}-{}{}'.format(f_release, f_num, file_ext))
        if write:
            try:
                rename(original_name, new_name)
            except FileExistsError:
                print(f'File "{new_name}" already exist!')
        else:
            return new_name
    else:
        return original_name


def files_rename(path=None, ext='.dwg'):
    if not path:
        path = workFolderApPath
    chdir(path)
    for f in [f for f in listdir(path) if f.lower().endswith(ext)]:
        file_rename(f)


def choice_request(func, *args, **kwargs):
    received_answer = input('"Enter" to process; "no" to decline: ').lower()
    if received_answer == 'no' or received_answer == 'n':
        print('Declined')
        return False
    else:
        print('Yes')
        func(args, **kwargs)
        return True


PROJECT_ROOT = r"\\mcp-fsvs2\Engineering\01 Projects"  # \\mcp-fsvs2\Engineering\01 Projects
WORK_ROOT = r"\\mcp-fsvs2\Production\_Programming_JOBS\_Turret Punch_"  # \\mcp-fsvs2\Production\_Programming_JOBS\_Turret Punch_

print('Write work and release number separated with space bar: \nexample: 1873 PAP 14A or 18112 MCM 06')
job, relType, relNum = re.findall(r'(^\d+|[a-zA-Z]+|\d+[a-zA-Z]?$)', input().upper())  # (^\d+|(?i)(pap|mcm)|\d+[a-z]?|[a-z]+$)
year = '20' + job[:2]  # 2018  (first 2 digits represent year)
print('Year:', year, '\nJob#', job, 'Release:', relType, relNum, "\n")

chdir(PROJECT_ROOT)
chdir(year)
for i in listdir():  # Seeking
    if i.startswith(job) and isdir(i):
        chdir(i)
        jobSrcFolder = getcwd()
        jobFolderName = i
        print(jobSrcFolder, '\t -->  !!!  FOUND  !!!')
        for j in listdir():
            if j in ['ID', 'IDs', 'PD', 'PDs'] and isdir(j):
                print('- ', j)
                for k in listdir(join(j)):
                    if k.find(relType) != -1 and k.endswith(relNum):
                        print('\t- ', k)
                        for l in listdir(join(j, k)):
                            print('\t\t- ', l)
                            if l.startswith('Spreadsheet'):
                                excelPath = join(getcwd(), j, k, l)
                        if j in ['PD', 'PDs']:
                            dwgFolderApPath = join(getcwd(), j, k)

print("Project fullname:", jobFolderName)
print("Source dwg folder:", dwgFolderApPath)
workFolderApPath = join(WORK_ROOT, year, jobFolderName, '%s %s' % (relType, relNum))
print("Work directory:", workFolderApPath)
if excelPath:
    print('Excel file path:', excelPath)
else:
    print('Excel file not found')

print(f'\nCopy files to work directory?')
answer = choice_request(files_transfer)
if answer:
    print('\nSimplify names of these files?')
    choice_request(files_rename)

print('\nWell done!')
