from h1 import generate_order
import requests
from data import MainUrl
import pytest

import allure
@pytest.mark.parametrize("color", [["BLACK"], ["GREY"], ["BLACK", "GREY"], [None]])
def test_create_orders(color):
	data1 = generate_order(color)
	response = requests.post(f"{MainUrl.order}", json=data1)
	
	assert response.status_code == 201