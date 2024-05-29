class CourierLogin:

    login_create = {
        "login": "qw2113192w2erty",
        "password": "12345",
        "firstName": "Fsaske"
    }

    login_equal = {
        "login": "qw2113192w2erty",
        "password": "111111",
        "firstName": "RLogin"
    }

    login_without_login = {
    "password": "12345",
    "firstName": "Fsaske"
    }

class VerificationCourierLogin:

    login_courier = {
        "login": "qw2113192w2erty",
        "password": "12345",
    }

    without_login = {
        "password": "12345"
    }

    without_password = {
        "login": "q29w2erty",
        "password": ""
    }

    incorrect_password = {
        "login": "q29w2erty",
        "password": "654654635"
    }

    incorrect_login = {
        "login": "q00029w2erty",
        "password": "12345"
    }

    existent_courier = {
        "login": "q029w2erty",
        "password": "1230045"
    }
    
class CreateOrders:
        data1 = {
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
        
        data2 = {
            "firstName": "Naruto",
            "lastName": "Uchiha",
            "address": "Konoha, 142 apt.",
            "metroStation": 4,
            "phone": "+7 800 355 35 35",
            "rentTime": 5,
            "deliveryDate": "2024-06-06",
            "comment": "Saske, come back to Konoha",
            "color": [
                "GREY"
            ]
        }
        
        data3 = {
            "firstName": "Naruto",
            "lastName": "Uchiha",
            "address": "Konoha, 142 apt.",
            "metroStation": 4,
            "phone": "+7 800 355 35 35",
            "rentTime": 5,
            "deliveryDate": "2024-06-06",
            "comment": "Saske, come back to Konoha",
            "color": [
                "GREY",
                "BLACK"
            ]
        }
        
        data4 = {
            "firstName": "Naruto",
            "lastName": "Uchiha",
            "address": "Konoha, 142 apt.",
            "metroStation": 4,
            "phone": "+7 800 355 35 35",
            "rentTime": 5,
            "deliveryDate": "2024-06-06",
            "comment": "Saske, come back to Konoha",
        }