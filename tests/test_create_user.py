import random
import allure
import pytest
import requests
import paths as paths
import messages as messages
import test_data as test_data
from request_helper import RequestHelper

class TestCreateUser:
    @allure.title('Проверка успешного создания уникальной учетной записи пользователя')
    @allure.step('Проверяем успешное создание пользователя')
    def test_create_user_positive_result(self):
        user = RequestHelper.create_user_request()
        response = requests.post(paths.REGISTER_URL, data=user)
        actual_result = response.json()
                
        assert 200 == response.status_code
        assert True == actual_result['success']
        
        token = actual_result['accessToken']
        requests.delete(paths.USER_URL, headers={'authorization': token})

    @allure.title('Проверка отправки запроса без обязательных полей')
    @allure.step('Проверяем, что пользователь не создается, если не отправить обязательные поля')
    @pytest.mark.parametrize('required_fields', test_data.required_fields)  
    def test_create_user_without_required_fields_negative_result(self, required_fields):
        response = requests.post(paths.REGISTER_URL, data=required_fields)
                
        assert 403 == response.status_code
        assert {"success":False, "message":messages.create_required_fields} == response.json()

    @allure.title('Проверка отправки запроса с существующим логином')
    @allure.step('Проверяем, что повторный пользователь не создается')    
    def test_create_repeat_user_already_used_result(self):
        user = RequestHelper.create_user_request()
        response = requests.post(paths.REGISTER_URL, data=user)
        r = response.json()
        token = r['accessToken']
        response_repeat = requests.post(paths.REGISTER_URL, data=user)
                
        assert 403 == response_repeat.status_code
        assert {"success":False, "message":messages.user_already_exists} == response_repeat.json()

        requests.delete(paths.USER_URL, headers={'authorization': token})
