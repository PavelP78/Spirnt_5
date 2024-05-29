import requests
import allure
from data import MainUrl


@allure.title('Проверка: в тело ответа возвращается список заказов')
def test_list_of_orders_answer():
	response = requests.get(MainUrl.order)
		
	assert response.json()['orders'] and response.status_code == 200