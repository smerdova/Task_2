import allure
import requests
import pytest
import paths as paths

class TestLoginUser:
    @allure.title('Проверка успешной авторизации пользователя')
    def test_login_user_positive_result(self, user_register):
        login = {}
        login['email'] = user_register['email']
        login['password'] = user_register['password']
        response_login = requests.post(paths.LOGIN_URL, data=login)  
        actual_result = response_login.json()
                
        assert 200 == response_login.status_code
        assert True == actual_result['success']

    login = [{
            "email": "", 
            "password": "12345"
        }, {
            "email": "test@gmail.com", 
            "password": ""
        }, {
            "email": "ndhsa14592145874964456987", 
            "password": "2145963"
        }]

    @allure.title('Проверка отправки запроса без обязательных полей и с некорректным логином и паролем')
    @pytest.mark.parametrize('login', login)  
    def test_login_user_without_required_fields_negative_result(self, login):
        response = requests.post(paths.LOGIN_URL, data=login)
        actual_result = response.json()
                
        assert 401 == response.status_code
        assert False == actual_result['success']
