import shutil


def unpack(archive_path, path_to_unpack):

    shutil.unpack_archive(archive_path, path_to_unpack)

    return None


archive_path = r'c:/GOIT/PYTHON/1_Python_core/module_06/backup_folder.zip'

path_to_unpack = r'c:/GOIT/PYTHON/1_Python_core/module_06/ex14'

unpack(archive_path, path_to_unpack)




'''
Створіть функціонал для розпакування архіву.

Зробіть import пакету shutil

Створіть функцію unpack(archive_path, path_to_unpack), яка викликатиме метод пакета shutil unpack_archive та розпаковуватиме архів archive_path у місце path_to_unpack.

Функція нічого не повертає.
'''