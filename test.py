from shutil import copy, copytree


def files_transfer(src, dest):
    copytree(src, dest, dirs_exist_ok=True)  # Флаг перезаписывает не спршивая. страшная сила.


srcFolder = r"D:\Users\Public\Downloads\01ProjectEmptyFiles\2017\1761 DEF, LLC\PD\Rel 001B"
destFolder = r"D:\Users\Public\Downloads\Dest folder"  # копирует только если папки не существует

files_transfer(srcFolder, destFolder)
