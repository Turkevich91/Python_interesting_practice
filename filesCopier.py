import os

projectsRoot = r"\\mcp-fsvs2\Engineering\01 Projects"
workRoot = r"\\mcp-fsvs2\Production\_Programming_JOBS\_Turret Punch_"

print('write work and release number using through space separator:')
# jobN, releaseN = '1873 PAP14'.split()  #
jobN, releaseN = input('1873 PAP14').split()
print('Job# ', jobN, 'Release: ', releaseN)
year = '20' + jobN[:2]  # 2018  (first 2 digits represent year)
print('Year: ', year)
os.chdir(projectsRoot)
os.chdir(year)
projectYear = os.getcwd()    # The current working directory to variable
folders = os.listdir(projectYear)
for i in folders:
    print(i)
    if i.startswith(jobN):
        projectFolder = os.path.join(projectYear, i)
        print('FOUND \n', projectFolder)
        for j in os.listdir(projectFolder):
            print('--- ', j)
            if j == "ID":
                for k in os.listdir(os.path.join(projectFolder, j)):
                    print('--- --- ', k)
            if j == "PD":
                for k in os.listdir(os.path.join(projectFolder, j)):
                    print('--- --- ', k)

print(projectFolder)
