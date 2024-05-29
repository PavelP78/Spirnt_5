import requests
import allure
from data import MainUrl
from  logins import CourierLogin, VerificationCourierLogin
from base.base_methods import HttpMethods

@allure.title('Проверка создания нового курьера')
def test_create_new_courier():
    response = HttpMethods.create_new_courier()
    assert response.status_code == 201
    response.delete = HttpMethods.delete_courier()

@allure.title('Проверка создания двух одинаковых курьеров')
def test_create_old_courier():
    response = HttpMethods.create_new_courier()
    response = HttpMethods.create_new_courier()
    assert response.status_code == 409
    response.delete = HttpMethods.delete_courier()

@allure.title('Проверка того, что успешный запрос возвращает "ok":true')
def test_create_courier_valid_answer():
    response = HttpMethods.create_new_courier()
    assert response.json() == {'ok': True}
    response.delete = HttpMethods.delete_courier()

@allure.title('Проверка создания курьера без поля login')
def test_create_courier_without_login():
    response = requests.post(f"{MainUrl.url}/api/v1/courier", data =VerificationCourierLogin.without_login)
    assert response.status_code == 400

@allure.title('Проверка того, что если создать пользователя с логином, который уже есть, возвращается ошибка.')
def test_create_courier_with_repeating_login():
    response = requests.post(f"{MainUrl.url}/api/v1/courier", data=CourierLogin.login_create)
    response = requests.post(f"{MainUrl.url}/api/v1/courier", data=CourierLogin.login_equal)
    assert response.status_code == 409
    response.delete = HttpMethods.delete_courier()
