import shutil
import os


def create_backup(path, file_name, employee_residence):

    full_path = f'{path}/{file_name}'
    with open(full_path, 'wb') as fh:
        for key, value in employee_residence.items():
            str = f'{key} {value}\n'
            b_str = str.encode()
            fh.write(b_str)
    
    # arh_path = r'c:/GOIT/PYTHON/1_Python_core/module_06'
    # arh_name = shutil.make_archive(os.path.join(arh_path, 'backup_folder'), 'zip', path)

    arh_name = shutil.make_archive('backup_folder', 'zip', path)

    return arh_name


path = r'c:/GOIT/PYTHON/1_Python_core/module_06/ex13'

file_name = 'file_ex_13.bin'

employee_residence = {'Michael': 'Canada', 'John':'USA', 'Liza': 'Australia'}


print(create_backup(path, file_name, employee_residence))


'''
Реалізуйте функцію create_backup(path, file_name, employee_residence)

Де:

path — шлях до файлу
file_name — ім'я файлу
employee_residence — словник, у якому ключ — ім'я користувача, а значення — країна проживання. Вигляд: {'Michael': 'Canada', 'John':'USA', 'Liza': 'Australia'}
Функція повинна працювати так:

1. Створювати бінарний файл file_name за шляхом path
2. Зберігати дані словника employee_residence у файл, де кожен новий рядок — це ключ значення через пробіл як "Michael Canada"
3. Архівувати теку по шляху path за допомогою shutil
4. Ім'я архіву має бути backup_folder.zip
5. Функція має повернути рядок шляху до архіву backup_folder.zip
Вимоги:

запишіть вміст словника employee_residence у бінарний файл з ім'ям file_name у теку path за допомогою оператора with.
використовуйте символ /, щоб розділити шлях для path та file_name
вигляд рядка файлу — Michael Canada, в кінці кожного рядка додається перенесення рядка '\n'.
при збереженні кожен рядок файлу кодується методом encode
при записі рядків використовуємо лише метод write
архів має бути у форматі zip з ім'ям 'backup_folder', створений за допомогою make_archive.
'''