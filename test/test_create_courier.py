import requests
import allure
from data import MainUrl
from logins import CourierLogin, VerificationCourierLogin
from base.base_methods import HttpMethods

@allure.title('Проверка создания нового курьера')
def test_create_new_courier(courier, delete_data_base):
    response = HttpMethods.create_new_courier()
    assert response.status_code == 201 



@allure.title('Проверка создания двух одинаковых курьеров')
def test_create_old_courier(courier, delete_data_base):
    response = HttpMethods.create_new_courier()
    response = HttpMethods.create_new_courier()
    assert response.status_code == 409



@allure.title('Проверка того, что успешный запрос на создание нового курьера возвращает "ok":true')
def test_create_courier_valid_answer(courier, delete_data_base):
    response = HttpMethods.create_new_courier()
    assert response.json() == {'ok': True}



@allure.title('Проверка создания курьера без поля login')
def test_create_courier_without_login():
    response = requests.post(f"{MainUrl.url}/api/v1/courier", data =VerificationCourierLogin.without_login)
    assert response.status_code == 400


@allure.title('Проверка того, что если создать пользователя с логином, который уже есть, возвращается ошибка.')
def test_create_courier_with_repeating_login(delete_data_base):
    response = requests.post(f"{MainUrl.url}/api/v1/courier", data=CourierLogin.login_create)
    response = requests.post(f"{MainUrl.url}/api/v1/courier", data=CourierLogin.login_equal)
    assert response.status_code == 409



@allure.title('Проверка создания курьера без поля password')
def test_create_courier_without_password():
    response = requests.post(f"{MainUrl.url}/api/v1/courier", data =VerificationCourierLogin.without_password)
    assert response.status_code == 400