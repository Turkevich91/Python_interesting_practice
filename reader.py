import os

os.chdir(r'P:\2019\19042\PAP 04') #получает список файлов в папке

for f in os.listdir():
    file_name, file_ext = os.path.splitext(f)
    f_job, f_release, f_num = file_name.split('-')

    f_job = f_job.strip()
    f_release = f_release.strip()
    f_num = f_num.strip()[1:].zfill(2)
    print('{}-{}-{}{}'.format(f_num, f_release, f_job, file_ext))