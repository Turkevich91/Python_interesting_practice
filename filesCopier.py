import os

projectsRoot = r"\\mcp-fsvs2\Engineering\01 Projects"

print('write work and release number using through space separator:')
jobN, releaseN = '1873 PAP14'.split()  # w = input().split()
print('Job# ', jobN, 'Release: ', releaseN)
year = '20' + jobN[:2]  # 2018  (first 2 digits represent year)
print('Year: ', year)
srcProjectRootPath = projectsRoot + '\\' + year   # this action requires domain permission
# on windows level
folders = os.listdir(srcProjectRootPath)
for i in folders:
    print(i)
    if i.startswith(jobN):
        projectFolder = srcProjectRootPath + '\\' + i
        print('FOUND \n', projectFolder)
        for j in os.listdir(projectFolder):
            print('--- ', j)


