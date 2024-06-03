import requests
import allure
from data import MainUrl, EndPoint


@allure.title('Проверка: в тело ответа возвращается список заказов')
def test_list_of_orders_answer():
	response = requests.get(MainUrl.url+EndPoint.create_orders)
	assert response.json()['orders'] and response.status_code == 200