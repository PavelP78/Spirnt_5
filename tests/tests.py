import requests
import allure
from data import MainUrl, EndPoint
from  logins import CourierLogin, VerificationCourierLogin, CreateOrders
from base.base_methods import HttpMethods
from json import dumps

@allure.title('Проверка: в тело ответа возвращается список заказов')
def test_list_of_orders_answer():
    response = HttpMethods.create_new_courier()  # создаем курьера
    response = HttpMethods.verification_courier() # авторизируем курьера для получения его id
    json_response = response.json()
    user_id = json_response['id'] # получаем id курьера и сохраняем в переменную user_id
    response = HttpMethods.create_orders() # создаем заказ
    json_response = response.json()
    orders_track = json_response['track']  # получаем track курьера и сохраняем в переменную orders_track
    
    response = requests.put(f"{MainUrl.url}/api/v1/orders/accept/{orders_track}", data={orders_track})  # принимаем заказ
    
    response = requests.get(f"{MainUrl.url}/api/v1/orders")  # получаем список заказов
    
    json_response = response.json()
    list_of_orders = json_response['orders']
    assert response.json() == {'orders': list_of_orders}  # проверка: в тело ответа возвращается список заказов
    
    response.delete = HttpMethods.delete_courier()