import pytest
import requests
from data import MainUrl, EndPoint
from  logins import CourierLogin, VerificationCourierLogin


@pytest.fixture
def courier():
    requests.post(f"{MainUrl.url}{EndPoint.create_courier}", data=CourierLogin.login_create)
    return courier


@pytest.fixture
def delete_data_base():
    response = requests.post(f"{MainUrl.url}{EndPoint.verification_courier}", data=VerificationCourierLogin.login_courier)
    json_response = response.json()
    user_id = json_response['id']
    requests.delete(f"{MainUrl.url}{EndPoint.delete_courier}{user_id}")
    return delete_data_base