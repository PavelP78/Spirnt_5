class CourierLogin:

    login_create = {
        "login": "qwerty0011",
        "password": "12345",
        "firstName": "Fsaske"
    }

    login_equal = {
        "login": "qwerty0011",
        "password": "111111",
        "firstName": "RLogin"
    }

    login_without_login = {
    "password": "12345",
    "firstName": "Fsaske"
    }

class VerificationCourierLogin:

    login_courier = {
        "login": "qwerty0011",
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
