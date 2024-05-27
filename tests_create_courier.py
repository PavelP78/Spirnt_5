import requests
import allure

url = 'https://qa-scooter.praktikum-services.ru'
data = {
    "login": "q29w2erty",
    "password": "12345",
    "firstName": "Fsaske"
}

@allure.title('Проверка создания нового курьера')
def test_create_new_courier():
    response = requests.post(f"{url}/api/v1/courier", data=data)
    assert response.status_code == 201

    response = requests.post(f"{url}/api/v1/courier/login", data=data)

    json_response = response.json()
    user_id = json_response['id']

    response.delete = requests.delete(f"{url}/api/v1/courier/{user_id}")

@allure.title('Проверка создания двух одинаковых курьеров')
def test_create_old_courier():
    response = requests.post(f"{url}/api/v1/courier", data=data)
    response = requests.post(f"{url}/api/v1/courier", data=data)
    assert response.status_code == 409

    response = requests.post(f"{url}/api/v1/courier/login", data=data)

    json_response = response.json()
    user_id = json_response['id']

    response.delete = requests.delete(f"{url}/api/v1/courier/{user_id}")

@allure.title('Проверка того, что успешный запрос возвращает "ok":true')
def test_create_courier_valid_answer():
    response = requests.post(f"{url}/api/v1/courier", data=data)
    assert response.json() == {'ok': True}


    response = requests.post(f"{url}/api/v1/courier/login", data=data)

    json_response = response.json()
    user_id = json_response['id']

    response.delete = requests.delete(f"{url}/api/v1/courier/{user_id}")

@allure.title('Проверка создания курьера без поля login')
def test_create_courier_without_login():
    response = requests.post(f"{url}/api/v1/courier", data = {
    "password": "12345",
    "firstName": "Fsaske"
    })
    assert response.status_code == 400

@allure.title('Проверка того, что если создать пользователя с логином, который уже есть, возвращается ошибка.')
def test_create_courier_with_repeating_login():
    response = requests.post(f"{url}/api/v1/courier", data=data)
    response = requests.post(f"{url}/api/v1/courier", data={
        "login": "q29w2erty",
        "password": "111111",
        "firstName": "RLogin"
        })
    assert response.status_code == 409

    response = requests.post(f"{url}/api/v1/courier/login", data=data)

    json_response = response.json()
    user_id = json_response['id']

    response.delete = requests.delete(f"{url}/api/v1/courier/{user_id}")
