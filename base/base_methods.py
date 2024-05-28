import requests
from data import MainUrl, EndPoint
from  logins import CourierLogin, VerificationCourierLogin

class HttpMethods:
    def create_new_courier():
        return requests.post(f"{MainUrl.url}{EndPoint.create_courier}", data=CourierLogin.login_create)

    def verification_courier():
        return requests.post(f"{MainUrl.url}{EndPoint.verification_courier}", data=VerificationCourierLogin.login_courier)

    def delete_courier():
        response = requests.post(f"{MainUrl.url}{EndPoint.verification_courier}", data=VerificationCourierLogin.login_courier)
        json_response = response.json()
        user_id = json_response['id']
        return requests.delete(f"{MainUrl.url}{EndPoint.delete_courier}{user_id}")