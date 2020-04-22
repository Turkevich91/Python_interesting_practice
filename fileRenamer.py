import os

path = input(r'')
print(os.listdir(path))
os.chdir(path)  # получает список файлов в папке

for f in os.listdir(path):
    # print('f = ', f)
    fPath = os.path.join(path, f)
    if os.path.isfile(fPath):
        file_name, file_ext = os.path.splitext(f)
        f_job, f_release, f_num = file_name.split('-')
        newName = ('{}-{}{}'.format(f_release, f_num, file_ext))
        print(newName)
        # print(f, '>', newName, '\n')
        os.rename(f, newName)
