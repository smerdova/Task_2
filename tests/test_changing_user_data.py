import random
import allure
import pytest
import requests
import paths as paths
import test_data as test_data
import messages as messages
from request_helper import RequestHelper

class TestChangingUserData:

    @allure.title('Проверка успешного изменения учетной записи пользователя с авторизацией')
    @allure.step('Проверяем успешное изменение учетной записи пользователя с авторизацией')
    @pytest.mark.parametrize('change_user_data', test_data.change_user_data)
    def test_changing_user_data_with_auth_positive_result(self, registered_user, change_user_data):
        response_change_user = requests.patch(paths.USER_URL, data=change_user_data, headers={'authorization': registered_user['accessToken']})
        actual_result = response_change_user.json()
                
        assert 200 == response_change_user.status_code
        assert True == actual_result['success']

    @allure.title('Проверка невозможности изменения учетной записи пользователя без авторизацией')
    @allure.step('Проверяем, что невозможно изменить учетную запись пользователя без авторизацией')
    def test_changing_user_data_without_auth_negative_result(self):
        change_user_data = RequestHelper.change_user_request()
        response_change_user = requests.patch(paths.USER_URL, data=change_user_data)
                        
        assert 401 == response_change_user.status_code
        assert {"success":False, "message":messages.authorization_required} == response_change_user.json()
