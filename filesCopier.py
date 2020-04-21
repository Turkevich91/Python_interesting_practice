import os

print('write work and release number using through space separator:')
w = '1873 PAP14'.split()  # w = input().split()
print(w)
year = '20' + w[0][:2]  # 2018  (first 2 digits represent year)
print(year)
srcProjectRootPath = r"\\mcp-fsvs2\Engineering\01 Projects" + '\\' + year   # this action requires domain permission
# on windows level
folders = os.listdir(srcProjectRootPath)
for i in folders:
    print(i)
