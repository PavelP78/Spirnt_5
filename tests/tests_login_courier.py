import requests
import allure
from data import MainUrl, CourierLogin, VerificationCourierLogin
from data import MainUrl, EndPoint

@allure.title('Проверка:  курьер может авторизоваться')
def test_verification_courier():
    response = requests.post(f"{MainUrl.url}/api/v1/courier", data=CourierLogin.login)
    response = requests.post(f"{MainUrl.url}/api/v1/courier/login", data=CourierLogin.login)
    assert response.status_code == 200
    
    json_response = response.json()
    user_id = json_response['id']

    response.delete = requests.delete(f"{MainUrl.url}/api/v1/courier/{user_id}")


@allure.title('Проверка ошибки авторизациии без ввода логин')
def test_verification_courier_without_login():
    response = requests.post(f"{MainUrl.url}/api/v1/courier", data=CourierLogin.login)
    response = requests.post(f"{MainUrl.url}/api/v1/courier/login", data=VerificationCourierLogin.without_login)
    assert response.status_code == 400
    
    response = requests.post(f"{MainUrl.url}/api/v1/courier/login", data=CourierLogin.login)
    json_response = response.json()
    user_id = json_response['id']
    response.delete = requests.delete(f"{MainUrl.url}/api/v1/courier/{user_id}")


@allure.title('Проверка ошибки авторизациии без ввода пароля')
def test_verification_courier_without_password():
    response = requests.post(f"{MainUrl.url}/api/v1/courier", data=CourierLogin.login)
    response = requests.post(f"{MainUrl.url}/api/v1/courier/login", data=VerificationCourierLogin.without_password)
    assert response.status_code == 400
    
    response = requests.post(f"{MainUrl.url}/api/v1/courier/login", data=CourierLogin.login)
    json_response = response.json()
    user_id = json_response['id']
    response.delete = requests.delete(f"{MainUrl.url}/api/v1/courier/{user_id}")


@allure.title('Cистема вернёт ошибку, если неправильно указать пароль')
def test_verification_courier_use_incorrect_password():
    response = requests.post(f"{MainUrl.url}/api/v1/courier", data=CourierLogin.login)
    response = requests.post(f"{MainUrl.url}/api/v1/courier/login", data=VerificationCourierLogin.incorrect_password)
    assert response.status_code == 404
    
@allure.title('Cистема вернёт ошибку, если неправильно указать логин')
def test_verification_courier_use_incorrect_login():
    response = requests.post(f"{MainUrl.url}/api/v1/courier", data=CourierLogin.login)
    response = requests.post(f"{MainUrl.url}/api/v1/courier/login", data=VerificationCourierLogin.incorrect_login)
    assert response.status_code == 404
    
@allure.title('Тест на попутку авторизоваться под несуществующим пользователем')
def test_verification_not_existent_courier():
    response = requests.post(f"{MainUrl.url}/api/v1/courier", data=CourierLogin.login)
    response = requests.post(f"{MainUrl.url}/api/v1/courier/login", data=VerificationCourierLogin.existent_courier)
    assert response.status_code == 404

@allure.title('Проверка:  успешный запрос возвращает id')
def test_verification_courier_answer():
    response = requests.post(f"{MainUrl.url}/api/v1/courier", data=CourierLogin.login)
    response = requests.post(f"{MainUrl.url}/api/v1/courier/login", data=CourierLogin.login)
 
    json_response = response.json()
    user_id = json_response['id']
    assert response.json() == {'id': user_id}
    response.delete = requests.delete(f"{MainUrl.url}/api/v1/courier/{user_id}")
    
     