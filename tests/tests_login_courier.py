import requests
import allure

url = 'https://qa-scooter.praktikum-services.ru'
data = {
    "login": "q29w2erty",
    "password": "12345",
    "firstName": "Fsaske"
}

@allure.title('Проверка:  курьер может авторизоваться')
def test_verification_courier():
    response = requests.post(f"{url}/api/v1/courier", data=data)
    response = requests.post(f"{url}/api/v1/courier/login", data=data)
    assert response.status_code == 200
    
    json_response = response.json()
    user_id = json_response['id']

    response.delete = requests.delete(f"{url}/api/v1/courier/{user_id}")


@allure.title('Проверка ошибки авторизациии без ввода логин')
def test_verification_courier_without_login():
    response = requests.post(f"{url}/api/v1/courier", data=data)
    response = requests.post(f"{url}/api/v1/courier/login", data={
        "password": "12345"
        })
    assert response.status_code == 400
    
    response = requests.post(f"{url}/api/v1/courier/login", data=data)
    json_response = response.json()
    user_id = json_response['id']
    response.delete = requests.delete(f"{url}/api/v1/courier/{user_id}")


@allure.title('Проверка ошибки авторизациии без ввода пароля')
def test_verification_courier_without_password():
    response = requests.post(f"{url}/api/v1/courier", data=data)
    response = requests.post(f"{url}/api/v1/courier/login", data={
        "login": "q29w2erty",
        "password": ""
    })
    assert response.status_code == 400
    
    response = requests.post(f"{url}/api/v1/courier/login", data=data)
    json_response = response.json()
    user_id = json_response['id']
    response.delete = requests.delete(f"{url}/api/v1/courier/{user_id}")


@allure.title('Cистема вернёт ошибку, если неправильно указать пароль')
def test_verification_courier_use_incorrect_password():
    response = requests.post(f"{url}/api/v1/courier", data=data)
    response = requests.post(f"{url}/api/v1/courier/login", data={
        "login": "q29w2erty",
        "password": "654654635"
    })
    assert response.status_code == 404
    
@allure.title('Cистема вернёт ошибку, если неправильно указать логин')
def test_verification_courier_use_incorrect_login():
    response = requests.post(f"{url}/api/v1/courier", data=data)
    response = requests.post(f"{url}/api/v1/courier/login", data={
        "login": "q00029w2erty",
        "password": "12345"
    })
    assert response.status_code == 404
    
@allure.title('Тест на попутку авторизоваться под несуществующим пользователем')
def test_verification_not_existent_courier():
    response = requests.post(f"{url}/api/v1/courier", data=data)
    response = requests.post(f"{url}/api/v1/courier/login", data={
        "login": "q029w2erty",
        "password": "1230045"
    })
    assert response.status_code == 404

@allure.title('Проверка:  успешный запрос возвращает id')
def test_verification_courier_answer():
    response = requests.post(f"{url}/api/v1/courier", data=data)
    response = requests.post(f"{url}/api/v1/courier/login", data=data)
 
    json_response = response.json()
    user_id = json_response['id']
    assert response.json() == {'id': user_id}
    response.delete = requests.delete(f"{url}/api/v1/courier/{user_id}")
    
     