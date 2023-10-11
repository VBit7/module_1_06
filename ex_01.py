def total_salary(path: str) -> float:
    fh = open(path, 'r')
    sum = 0
    try:
        while True:
            line = fh.readline()
            # sum += float(line.split(','))
            if not line:
                break
            sum += int(line.split(',')[-1].rstrip())
    finally:
        fh.close()

    return float(sum)


path_salary = r'c:\GOIT\PYTHON\1_Python_core\module_06\file_ex_01.txt'

print(total_salary(path_salary))



'''
Нехай ми маємо текстовий файл, який містить дані з місячною заробітною платою по кожному розробнику компанії.

Приклад файлу:

Alex Korp,3000
Nikita Borisenko,2000
Sitarama Raju,1000
Як бачимо, структура файлу – це прізвище розробника та значення його заробітної плати, розділеної комою.

Розробіть функцію total_salary(path) (параметр path - шлях до файлу), яка буде розбирати текстовий файл і повертати загальну суму заробітної плати всіх розробників компанії.

Вимоги до завдання:

функція total_salary повертає значення типу float
для читання файлу функція total_salary використовує лише метод readline
ми поки що не використовуємо менеджер контексту with
'''