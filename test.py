import os
from shutil import copy, copytree


def file_transfer():
    copytree(src, dest, dirs_exist_ok=True)  # Флаг перезаписывает не спршивая. страшная сила.


src = r"D:\Users\Public\Downloads\01ProjectEmptyFiles\2017\1761 DEF, LLC\PD\Rel 001B"
dest = r"D:\Users\Public\Downloads\Dest folder"  # копирует только если папки не существует

file_transfer()
