def read_employees_from_file(path):
    list_result =[]
    fh = open(path, 'r')
    try:
        while True:
            line = fh.readline()
            if not line:
                break
            list_result.append(line.rstrip())
    finally:
        fh.close()

    return list_result


path_read = r'c:\GOIT\PYTHON\1_Python_core\module_06\file_ex_02.txt'

print(read_employees_from_file(path_read))



'''
У попередній задачі ми записали співробітників у файл у такому вигляді:

Robert Stivenson,28
Alex Denver,30
Drake Mikelsson,19
Виконаємо тепер зворотнє завдання і створимо функцію read_employees_from_file(path), яка читатиме дані з файлу та повертатиме список співробітників у вигляді:

['Robert Stivenson,28', 'Alex Denver,30', 'Drake Mikelsson,19']
Пам'ятайте про наявність символу кінця рядка \n під час читання даних із файлу. Його необхідно прибирати при додаванні прочитаного рядка до списку.

Вимоги:

прочитайте вміст файлу за допомогою режиму "r".
ми поки що не використовуємо менеджер контексту with
поверніть із функції список співробітників із файлу
'''