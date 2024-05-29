import pytest
from helper import generate_random_order
import requests
from data import MainUrl

@pytest.mark.parametrize("color", [["BLACK"], ["GREY"], ["BLACK", "GREY"], [None]])
def test_create_orders(color):
    random_order = generate_random_order()
    response = requests.post(f"{MainUrl.order}", json=random_order)
    
    
    assert response.status_code == 201