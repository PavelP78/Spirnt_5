import requests
import allure
from json import dumps

url = 'https://qa-scooter.praktikum-services.ru'
data1 = {
	"firstName": "Naruto",
    "lastName": "Uchiha",
    "address": "Konoha, 142 apt.",
    "metroStation": 4,
    "phone": "+7 800 355 35 35",
    "rentTime": 5,
    "deliveryDate": "2024-06-06",
    "comment": "Saske, come back to Konoha",
    "color": [
        "BLACK"
    ]
}

data2 = {
	"firstName": "Naruto",
    "lastName": "Uchiha",
    "address": "Konoha, 142 apt.",
    "metroStation": 4,
    "phone": "+7 800 355 35 35",
    "rentTime": 5,
    "deliveryDate": "2024-06-06",
    "comment": "Saske, come back to Konoha",
    "color": [
        "GREY"
    ]
}

data3 = {
	"firstName": "Naruto",
    "lastName": "Uchiha",
    "address": "Konoha, 142 apt.",
    "metroStation": 4,
    "phone": "+7 800 355 35 35",
    "rentTime": 5,
    "deliveryDate": "2024-06-06",
    "comment": "Saske, come back to Konoha",
    "color": [
        "GREY",
 		"BLACK"
    ]
}

data4 = {
	"firstName": "Naruto",
    "lastName": "Uchiha",
    "address": "Konoha, 142 apt.",
    "metroStation": 4,
    "phone": "+7 800 355 35 35",
    "rentTime": 5,
    "deliveryDate": "2024-06-06",
    "comment": "Saske, come back to Konoha",
	}
@allure.title('Проверка создания заказа с цветом  BLACK')
def test_create_orders_with_black_color():
	response = requests.post(f"{url}/api/v1/orders", data=dumps(data1))
	assert response.status_code == 201
	

@allure.title('Проверка создания заказа с цветом  GREY')
def test_create_orders_with_grey_color():
	response = requests.post(f"{url}/api/v1/orders", data=dumps(data2))
	assert response.status_code == 201

@allure.title('Проверка создания заказа с цветом  GREY и BLACK')
def test_create_orders_with_grey_and_black_color():
	response = requests.post(f"{url}/api/v1/orders", data=dumps(data3))
	assert response.status_code == 201
	
@allure.title('Проверка создания заказа с цветом  GREY и BLACK')
def test_create_orders_without_color():
	response = requests.post(f"{url}/api/v1/orders", data=dumps(data4))
	assert response.status_code == 201
	
	
@allure.title('Проверка: тело ответа содержит track')
def test_create_orders_answer():
	response = requests.post(f"{url}/api/v1/orders", data=dumps(data4))
	
	json_response = response.json()
	orders_track = json_response['track']
	
	assert response.json() == {'track': orders_track}
