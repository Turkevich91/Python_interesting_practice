import os  # , shutil
import re


def file_transfer():
    pass


def file_rename(file_name):
    if len(file_name.split('-')) == 3:  # and os.path.isfile(file_name)
        file_name, file_ext = os.path.splitext(file_name)  # Делим файл на имя и расширение
        f_job, f_release, f_num = file_name.split('-')  # Делим имя файла по метке "-" на 3 части
        new_name = ('{}-{}{}'.format(f_release, f_num, file_ext))
        return new_name
    else:
        return file_name


def files_rename():
    path = dwgFolderApPath
    print(os.listdir(path))
    os.chdir(path)  # Смена текущей директории

    for f in [f for f in os.listdir(path) if f.lower().endswith('.dwg')]:
        print(f)
        file_rename(f)


def choice_request(func):
    answer = input('Press "Enter" to process or type "n" to decline').lower()
    if answer == 'no' or answer == 'n':
        print('Declined')
        return False
    else:
        func()
        print('Processed succeed')
        return True


projectsRoot = r"\\mcp-fsvs2\Engineering\01 Projects"
workRoot = r"\\mcp-fsvs2\Production\_Programming_JOBS\_Turret Punch_"

print('Write work and release number separated with space bar: \nexample: 1873 PAP 14A or 18112 MCM 06')
job, relType, relNum = re.findall(r'(^\d+|[a-zA-Z]+|\d+[a-zA-Z]?$)', input().upper())  # replace with input()
year = '20' + job[:2]  # 2018  (first 2 digits represent year)
print('Year:', year, '\nJob#', job, 'Release:', relType, relNum, "\n")

os.chdir(projectsRoot)
os.chdir(year)
for i in os.listdir():  # Siking
    if i.startswith(job) and os.path.isdir(i):
        os.chdir(i)
        jobSrcFolder = os.getcwd()
        jobFolderName = i
        print(jobSrcFolder, '\t -->  !!!  FOUND  !!!')
        for j in os.listdir():
            if (j == "ID" or j == "PD") and os.path.isdir(j):
                print('- ', j)
                for k in os.listdir(os.path.join(j)):
                    if k.find(relType) != -1 and k.endswith(relNum):
                        print('\t- ', k)
                        for l in os.listdir(os.path.join(j, k)):
                            print('\t\t- ', file_rename(l), 'rmd')
                            if l.startswith('Spreadsheet'):
                                excelPath = os.path.join(os.getcwd(), j, k, l)
                        if j == "PD":
                            dwgFolderApPath = os.path.join(os.getcwd(), j, k)

print("Project fullname:", jobFolderName)
print("Source dwg folder:", dwgFolderApPath)

try:
    print('Exelfile path:', excelPath)
except:
    print('Exelfile file not found')

workFolderApPath = os.path.join(workRoot, year, jobFolderName, '%s %s' % (relType, relNum))
# print("Work path:", workFolderApPath)

for i in range(1):
    print(f'\n??? Copy files to work directory ???\t({workFolderApPath})')
    choice_request(file_transfer)   # Надо сделать нормальное условие которое бы исключало второй
    # вопрос при отказе копирования файлов.
    if choice_request:
        print('\nDo you want to simplify names of these files?')
        choice_request(files_rename)

print('\nWell done!')
