import requests
import allure
from json import dumps
from data import MainUrl
from logins import CreateOrders


@allure.title('Проверка создания заказа с цветом  BLACK')
def test_create_orders_with_black_color():
	response = requests.post(f"{MainUrl.url}/api/v1/orders", data=dumps(CreateOrders.data1))
	assert response.status_code == 201
	

@allure.title('Проверка создания заказа с цветом  GREY')
def test_create_orders_with_grey_color():
	response = requests.post(f"{MainUrl.url}/api/v1/orders", data=dumps(CreateOrders.data2))
	assert response.status_code == 201

@allure.title('Проверка создания заказа с цветом  GREY и BLACK')
def test_create_orders_with_grey_and_black_color():
	response = requests.post(f"{MainUrl.url}/api/v1/orders", data=dumps(CreateOrders.data3))
	assert response.status_code == 201
	
@allure.title('Проверка создания заказа с цветом  GREY и BLACK')
def test_create_orders_without_color():
	response = requests.post(f"{MainUrl.url}/api/v1/orders", data=dumps(CreateOrders.data4))
	assert response.status_code == 201
	
	
@allure.title('Проверка: тело ответа содержит track')
def test_create_orders_answer():
	response = requests.post(f"{MainUrl.url}/api/v1/orders", data=dumps(CreateOrders.data4))
	
	json_response = response.json()
	orders_track = json_response['track']
	
	assert response.json() == {'track': orders_track}
