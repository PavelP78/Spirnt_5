import requests
import allure
from data import MainUrl, EndPoint
from  logins import CourierLogin, VerificationCourierLogin


@allure.title('Проверка создания нового курьера')
def test_create_new_courier():
    response = requests.post(f"{MainUrl.url}{EndPoint.create_courier}", data=CourierLogin.login_create)
    assert response.status_code == 201

    response = requests.post(f"{MainUrl.url}{EndPoint.verification_courier}", data=VerificationCourierLogin.login_courier)

    json_response = response.json()
    user_id = json_response['id']

    response.delete = requests.delete(f"{MainUrl.url}{EndPoint.delete_courier}{user_id}")

@allure.title('Проверка создания двух одинаковых курьеров')
def test_create_old_courier():
    response = requests.post(f"{MainUrl.url}/api/v1/courier", data=CourierLogin.login)
    response = requests.post(f"{MainUrl.url}/api/v1/courier", data=CourierLogin.login)
    assert response.status_code == 409

    response = requests.post(f"{MainUrl.url}/api/v1/courier/login", data=CourierLogin.login)

    json_response = response.json()
    user_id = json_response['id']

    response.delete = requests.delete(f"{MainUrl.url}/api/v1/courier/{user_id}")

@allure.title('Проверка того, что успешный запрос возвращает "ok":true')
def test_create_courier_valid_answer():
    response = requests.post(f"{MainUrl.url}/api/v1/courier", data=CourierLogin.login)
    assert response.json() == {'ok': True}


    response = requests.post(f"{MainUrl.url}/api/v1/courier/login", data=CourierLogin.login)

    json_response = response.json()
    user_id = json_response['id']

    response.delete = requests.delete(f"{MainUrl.url}/api/v1/courier/{user_id}")

@allure.title('Проверка создания курьера без поля login')
def test_create_courier_without_login():
    response = requests.post(f"{MainUrl.url}/api/v1/courier", data =CourierLogin.login_without_login)
    assert response.status_code == 400

@allure.title('Проверка того, что если создать пользователя с логином, который уже есть, возвращается ошибка.')
def test_create_courier_with_repeating_login():
    response = requests.post(f"{MainUrl.url}/api/v1/courier", data=CourierLogin.login)
    response = requests.post(f"{MainUrl.url}/api/v1/courier", data=CourierLogin.login_equal)
    assert response.status_code == 409

    response = requests.post(f"{MainUrl.url}/api/v1/courier/login", data=CourierLogin.login)

    json_response = response.json()
    user_id = json_response['id']

    response.delete = requests.delete(f"{MainUrl.url}/api/v1/courier/{user_id}")
