import configuration

import requests

import data

# Определение функции post_new_user для отправки POST-запроса на создание нового пользователя
def post_new_user(body):
    # Выполнение POST-запроса с использованием URL из конфигурационного файла, тела запроса и заголовков
    # URL_SERVICE и CREATE_USER_PATH объединяются для формирования полного URL для запроса
    # json=body используется для отправки данных пользователя в формате JSON
    # headers=data.headers устанавливает заголовки запроса из модуля data
    return requests.post(configuration.URL_SERVICE + configuration.CREATE_USER_PATH,
                         json=body,
                         headers=data.headers)

# Вызов функции post_new_user с телом запроса для создания нового пользователя из модуля data
user_response = post_new_user(data.user_body)

# Вывод HTTP-статус кода ответа на запрос
# Код состояния указывает на результат обработки запроса сервером
print(user_response.status_code)

# Функция response.json() позволяет получить тело ответа в формате JSON.
# Это полезно для извлечения данных, полученных в результате запроса,
# особенно когда сервер возвращает полезные данные в формате JSON.
# Здесь мы вызываем эту функцию и выводим полученный JSON в консоль для наглядности.
print(user_response.json())

# Определение функции post_new_client_kit для отправки POST-запроса на создание нового набора
def post_new_client_kit(body):
    # Выполнение POST-запроса с использованием URL из конфигурационного файла, тела запроса и заголовков
    return requests.post(configuration.URL_SERVICE + configuration.CREATE_KIT_NAME,
                         json=body,
                         headers=data.headers_kit)


# Вызов функции post_new_client_kit с телом запроса для создания нового набора из модуля data
kit_response = post_new_client_kit(data.kit_body)