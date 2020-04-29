import os, re

def file_rename(file_name):
    if len(file_name.split('-')) == 3:  #  and os.path.isfile(file_name)
        file_name, file_ext = os.path.splitext(file_name)  # Делим файл на имя и расширение
        f_job, f_release, f_num = file_name.split('-')  # Делим имя файла по метке "-" на 3 части
        new_name = ('{}-{}{}'.format(f_release, f_num, file_ext))
        # print(newName)
        # print(file_name, ' > ', new_name)
        return new_name
        # os.rename(f, newName) # Раскоментировать перед применением

projectsRoot = r"\\mcp-fsvs2\Engineering\01 Projects"
workRoot = r"\\mcp-fsvs2\Production\_Programming_JOBS\_Turret Punch_"

print('Write work and release number separated with space bar: \nexample: 1873 PAP 14A or 18112 MCM 06')
job, relType, relNum = re.findall(r'(^\d+|[a-zA-Z]+|\d+[a-zA-Z]?$)', '1873 PAP08')  # replace with input()
year = '20' + job[:2]  # 2018  (first 2 digits represent year)
print('Job#', job, 'Release:', relType, relNum, "\n" 'Year:', year)
os.chdir(projectsRoot)
os.chdir(year)
for i in os.listdir():  # Siking
    print(i)
    if i.startswith(job) and os.path.isdir(i):
        jobSrcFolder = os.path.join(i)
        jobFolderName = i
        print('FOUND \n', jobSrcFolder)
        for j in os.listdir(jobSrcFolder):
            print('---| ', j)
            if j == "ID":  # при нахождении этой папки скопировать путь файла
                for k in os.listdir(os.path.join(jobSrcFolder, j)):
                    print('\t---| ', k)
                    if k.find(relType) != -1 and k.endswith(relNum):
                        for l in os.listdir(os.path.join(jobSrcFolder, j, k)):
                            print('\t\t---| ', l)
            if j == "PD":
                for k in os.listdir(os.path.join(jobSrcFolder, j)):
                    print('\t---| ', k)
                    if k.find(relType) != -1 and k.endswith(relNum):
                        dwgFolder = os.path.join(jobSrcFolder, j, k)
                        for l in os.listdir(os.path.join(jobSrcFolder, j, k)):
                            print('\t\t---| ', l + " >", file_rename(l))

print(os.path.abspath(jobSrcFolder))
print("dwg source folder:", os.path.join(projectsRoot, year, dwgFolder))
print(jobFolderName)