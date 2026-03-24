import allure
import requests
import pytest
import paths as paths
import test_data as test_data
from request_helper import RequestHelper

class TestLoginUser:
    @allure.title('Проверка успешной авторизации пользователя')
    @allure.step('Проверяем успешную авторизацию пользователя')
    def test_login_user_positive_result(self, registered_user):
        login = RequestHelper.login_user_request(registered_user['email'], registered_user['password'])
        response_login = requests.post(paths.LOGIN_URL, data=login)  
        actual_result = response_login.json()
                
        assert 200 == response_login.status_code
        assert True == actual_result['success']

    @allure.title('Проверка отправки запроса без обязательных полей и с некорректным логином и паролем')
    @allure.step('Проверяем, что нельзя отправить запрос на авторизацию без обязательных полей и с некорректным логином и паролем')
    @pytest.mark.parametrize('login', test_data.login)  
    def test_login_user_without_required_fields_negative_result(self, login):
        response = requests.post(paths.LOGIN_URL, data=login)
        actual_result = response.json()
                
        assert 401 == response.status_code
        assert False == actual_result['success']
