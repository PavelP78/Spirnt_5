import requests
import allure
from  logins import CourierLogin, VerificationCourierLogin
from data import MainUrl, EndPoint
from base.base_methods import HttpMethods


@allure.title('Проверка:  курьер может авторизоваться')
def test_verification_courier(courier):
    response = HttpMethods.verification_courier()
    assert response.status_code == 200
    response.delete = HttpMethods.delete_courier()


@allure.title('Проверка ошибки авторизациии без ввода логин')
def test_verification_courier_without_login(courier, delete_data_base):
    response = requests.post(f"{MainUrl.url}/api/v1/courier/login", data=VerificationCourierLogin.without_login)
    assert response.status_code == 400



@allure.title('Проверка ошибки авторизациии без ввода пароля')
def test_verification_courier_without_password(courier, delete_data_base):
    response = requests.post(f"{MainUrl.url}/api/v1/courier/login", data=VerificationCourierLogin.without_password)
    assert response.status_code == 400



@allure.title('Cистема вернёт ошибку, если неправильно указать пароль')
def test_verification_courier_use_incorrect_password(courier):
    response = requests.post(f"{MainUrl.url}/api/v1/courier/login", data=VerificationCourierLogin.incorrect_password)
    assert response.status_code == 404


@allure.title('Cистема вернёт ошибку, если неправильно указать логин')
def test_verification_courier_use_incorrect_login(courier):
    response = requests.post(f"{MainUrl.url}/api/v1/courier/login", data=VerificationCourierLogin.incorrect_login)
    assert response.status_code == 404


@allure.title('Тест на попытку авторизоваться под несуществующим пользователем')
def test_verification_not_existent_courier():
    response = requests.post(f"{MainUrl.url}/api/v1/courier/login", data=VerificationCourierLogin.existent_courier)
    assert response.status_code == 404


@allure.title('Проверка:  успешный запрос при верификации курьера возвращает id курьера')
def test_verification_courier_answer():
    response = requests.post(f"{MainUrl.url}/api/v1/courier", data=CourierLogin.login_create)
    response = requests.post(f"{MainUrl.url}/api/v1/courier/login", data=VerificationCourierLogin.login_courier)
    json_response = response.json()
    user_id = json_response['id']
    assert response.json() == {'id': user_id}
    response.delete = requests.delete(f"{MainUrl.url}/api/v1/courier/{user_id}")
    