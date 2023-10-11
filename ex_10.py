def save_credentials_users(path: str, users_info: dict):

    with open(path, 'wb') as fh:
        for key, value in users_info.items():
            key_b = key.encode('utf-8')
            value_b = value.encode('utf-8')
            fh.write(key_b + b':' + value_b + b'\n')

    return None


dict_user_info = {'andry':'uyro18890D', 'steve':'oppjM13LL9e'}

path_write = r'c:\GOIT\PYTHON\1_Python_core\module_06\file_ex_10.bin'

save_credentials_users(path_write, dict_user_info)



'''
Дані про користувачів краще зберігати у форматі бінарних файлів. Тому вам необхідно створити функцію, яка буде записувати логін та пароль користувача у файл.

Реалізуйте функцію save_credentials_users(path, users_info), яка зберігає інформацію про користувачів з паролями в бінарний файл.

Де:

path – шлях до файлу.
users_info - словник типу {'andry':'uyro18890D', 'steve':'oppjM13LL9e'}, де ключ — логін (username) користувача, а значення — його пароль (password).
Вимоги:

Кожен рядок файлу повинен мати такий вигляд username:password. Такий формат запису використовують при Базовій аутентифікації.
Відкрийте файл для запису та збережіть ключ та значення зі словника users_info у вигляді окремого рядка username:password для кожного елемента словника users_info
'''