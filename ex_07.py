from re import sub

def sanitize_file(source: str, output: str):
    
    with open(source, 'r') as fh_read:
        all_file = sub(r'\d', '', fh_read.read())

    with open(output, 'w') as fh_write:
        fh_write.write(all_file)

    return None


path_read  = r'c:\GOIT\PYTHON\1_Python_core\module_06\file_ex_07_r.txt'
path_write = r'c:\GOIT\PYTHON\1_Python_core\module_06\file_ex_07_w.txt'

sanitize_file(path_read, path_write)



'''
Розробіть функцію sanitize_file(source, output), що переписує у текстовий файл output вміст текстового файлу source, очищений від цифр.

Вимоги:

- прочитайте вміст файлу source, використовуючи менеджер контексту with та режим "r".
- запишіть новий очищений від цифр вміст файлу output, використовуючи менеджер контексту with та режим "w"
- запис нового вмісту файлу output має бути одноразовий і використовувати метод write
'''