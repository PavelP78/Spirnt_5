import requests
import allure
from data import MainUrl, EndPoint
from  logins import CourierLogin, VerificationCourierLogin
from base.base_methods import HttpMethods

@allure.title('Проверка создания нового курьера')
def test_create_new_courier():
    response = HttpMethods.create_new_courier()
    assert response.status_code == 201
    response.delete = HttpMethods.delete_courier()