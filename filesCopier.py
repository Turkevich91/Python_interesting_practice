import os

projectRoot = r"\\mcp-fsvs2\Engineering\01 Projects"
workRoot = r"\\mcp-fsvs2\Production\_Programming_JOBS\_Turret Punch_"

print('write work and release number using through space separator:')
# jobN, releaseN = '1873 PAP14'.split()  #
jobN, releaseN = input().split()
print('Job# ', jobN, 'Release: ', releaseN)
year = '20' + jobN[:2]  # 2018  (first 2 digits represent year)
print('Year: ', year)
projectYear = os.path.join(projectRoot, year)    # this action requires domain permission
# on windows level
folders = os.listdir(projectYear)
for i in folders:
    print(i)
    if i.startswith(jobN):
        projectFolder = os.path.join(projectYear, i)
        print('FOUND \n', projectFolder)
        for j in os.listdir(projectFolder):
            print('--- ', j)

print(projectFolder)
print(os.listdir(os.path.join(workRoot, year)))


