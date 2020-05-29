# from shutil import copy, copytree
#
#
# def files_transfer(src, dest):
#     copytree(src, dest, dirs_exist_ok=True)  # Флаг перезаписывает не спршивая. страшная сила.
#
#
# srcFolder = r"D:\Users\Public\Downloads\01ProjectEmptyFiles\2017\1761 DEF, LLC\PD\Rel 001B"
# destFolder = r"D:\Users\Public\Downloads\Dest folder"  # копирует только если папки не существует
#
# files_transfer(srcFolder, destFolder)


from random import randint

s = 'RSP'
stop = False

while not stop:
    random = randint(0, 2)
    getValue = s.index(input('chose one letter from string "RSP" ').upper())
    print("CPU:", s[random], "Player:", s[getValue])
    if random == getValue:
        print('dead heat')
    elif s[random - 1] == s[getValue]:
        print('You Won')
    else:
        print('You lose')

    print('\nplay again? "n" to stop: ')
    if input() == "n":
        stop = True
