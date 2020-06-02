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


def input_checker(s):
    user_input = input(f'chose one letter from string "{s}" ').upper()
    if user_input in s and user_input not in "":
        return sampleSTR.index(user_input)
    else:
        print('Wrong input, try again')
        input_checker(s)


sampleSTR = 'RSP'
stop = False

while not stop:
    random = randint(0, 2)
    getValue = input_checker(sampleSTR)
    print("CPU:", sampleSTR[random], "Player:", sampleSTR[getValue])
    if random == getValue:
        print('dead heat')
    elif sampleSTR[random - 1] == sampleSTR[getValue]:
        print('You Won')
    else:
        print('You lose')

    print('\nplay again? "n" to stop: ')
    if input() == "n":
        stop = True
