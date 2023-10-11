import base64


def encode_data_to_base64(data):

    list_result = []

    for item in data:
        list_result.append(base64.b64encode(item.encode('utf-8')).decode('utf-8'))
    
    return list_result


list_data = ['andry:uyro18890D', 'steve:oppjM13LL9e']

print(encode_data_to_base64(list_data))



'''
Функція get_credentials_users із попереднього завдання повертає нам список рядків username:password:

['andry:uyro18890D', 'steve:oppjM13LL9e']
Реалізуйте функцію encode_data_to_base64(data), яка приймає у параметрі data зазначений список,
виконує кодування кожної пари username:password у формат Base64 та повертає список із закодованими парами username:password у вигляді:

['YW5kcnk6dXlybzE4ODkwRA==', 'c3RldmU6b3Bwak0xM0xMOWU=']
'''