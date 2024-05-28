import requests
import allure
from json import dumps

url = 'https://qa-scooter.praktikum-services.ru'
orders = {
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
data = {
    "login": "q29w2erty",
    "password": "12345",
    "firstName": "Fsaske"
}

login = {
    "login": "q29w2erty",
    "password": "12345"
}

@allure.title('Проверка: в тело ответа возвращается список заказов')
def test_list_of_orders_answer():
	response = requests.post(f"{url}/api/v1/courier", data=data) # создаем курьера
	
	response = requests.post(f"{url}/api/v1/courier/login", data=login) # авторизируем курьера для получения его id
	json_response = response.json()
	user_id = json_response['id'] # получаем id курьера и сохраняем в переменную user_id
	
	response = requests.post(f"{url}/api/v1/orders", data=dumps(orders)) # создаем заказ
	json_response = response.json()
	orders_track = json_response['track'] # получаем track курьера и сохраняем в переменную orders_track
	

	response = requests.put(f"{url}/api/v1/orders/accept/{orders_track}", data=/v1/orders/accept/{user_id}) # принимаем заказ
	
	response = requests.get(f"{url}/api/v1/orders") # получаем список заказов
	
	json_response = response.json()
	list_of_orders = json_response['orders']
	assert response.json() == {'orders': list_of_orders} # проверка: в тело ответа возвращается список заказов

	response.delete = requests.delete(f"{url}/api/v1/courier/{user_id}") # удаляем курьера
	