import os, re

projectsRoot = r"\\mcp-fsvs2\Engineering\01 Projects"
workRoot = r"\\mcp-fsvs2\Production\_Programming_JOBS\_Turret Punch_"

print('write work and release number using through space separator: \nexample: 1873 PAP14')
job, release = '1873 PAP14'.split()  #
# job, release = input().split()
year = '20' + job[:2]  # 2018  (first 2 digits represent year)
print('Job# ', job, 'Release: ', release, "\n" 'Year: ', year)
os.chdir(projectsRoot)
os.chdir(year)
for i in os.listdir():   # Siking
    print(i)
    if i.startswith(job) and os.path.isdir(i):
        jobFolder = os.path.join(i)
        print('FOUND \n', jobFolder)
        for j in os.listdir(jobFolder):
            print('---| ', j)
            if j == "ID":   # при нахождении этой папки скопировать путь файла
                for k in os.listdir(os.path.join(jobFolder, j)):
                    print('\t---| ', k)
            if j == "PD":
                for k in os.listdir(os.path.join(jobFolder, j)):
                    print('\t---| ', k)


print(os.path.abspath(jobFolder))
