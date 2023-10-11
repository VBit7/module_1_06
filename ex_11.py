def get_credentials_users(path):

    list_result = []

    with open(path, 'rb') as fh:
        while True:
            line = fh.readline()
            if not line:
                break
            list_result.append(line.decode('utf-8').rstrip())
    
    return list_result


path_read = r'c:\GOIT\PYTHON\1_Python_core\module_06\file_ex_10.bin'

print(get_credentials_users(path_read))



'''
Реалізуйте функцію get_credentials_users(path), яка повертає список рядків із бінарного файлу, створеного в попередньому завданню, де:

path – шлях до файлу.
Формат файлу:

andry:uyro18890D
steve:oppjM13LL9e
Відкрийте файл для читання, використовуючи with та режим rb. Сформуйте список рядків із файлу та поверніть його з функції get_credentials_users у наступному форматі:

['andry:uyro18890D', 'steve:oppjM13LL9e']
Вимоги:

Використовуйте менеджер контексту для читання з файлу
'''