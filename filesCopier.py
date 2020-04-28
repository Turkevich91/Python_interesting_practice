import os

projectsRoot = r"\\mcp-fsvs2\Engineering\01 Projects"
workRoot = r"\\mcp-fsvs2\Production\_Programming_JOBS\_Turret Punch_"

print('write work and release number using through space separator:')
# jobN, releaseN = '1873 PAP14'.split()  #
job, release = input('example: \n1873 PAP14').split()
year = '20' + job[:2]  # 2018  (first 2 digits represent year)
print('Job# ', job, 'Release: ', release, "\n" 'Year: ', year)
os.chdir(projectsRoot)
os.chdir(year)
# os.chdir(r'C:\Sandbox\vetal\DefaultBox\user\current\AppData\Local\Microsoft\Windows\Explorer')
for i in os.listdir():   # Siking
    print(i)
    if i.startswith(job) and os.path.isdir(i):
        jobFolder = os.path.join(os.getcwd(), i)
        print('FOUND \n', jobFolder)
        for j in os.listdir(jobFolder):
            print('--- ', j)
            if j == "ID":
                for k in os.listdir(os.path.join(jobFolder, j)):
                    print('--- --- ', k)
            if j == "PD":
                for k in os.listdir(os.path.join(jobFolder, j)):
                    print('--- --- ', k)
