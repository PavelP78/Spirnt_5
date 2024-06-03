from helper import generate_order
import requests
from data import MainUrl, EndPoint
import pytest
import allure


@allure.title('Проверка создания заказа')
@pytest.mark.parametrize("color", [["BLACK"], ["GREY"], ["BLACK", "GREY"], [None]])
def test_create_orders(color):
	data1 = generate_order(color)
	response = requests.post(f"{MainUrl.url}{EndPoint.create_orders}", json=data1)
	assert response.status_code == 201
