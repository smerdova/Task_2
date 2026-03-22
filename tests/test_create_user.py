import random
import allure
import pytest
import requests
import paths as paths
import messages as messages

class TestCreateUser:
    @allure.title('Проверка успешного создания уникальной учетной записи пользователя')
    def test_create_user_positive_result(self):
        user = {}
        user['email'] = f"user{random.randint(1, 999999999)}@gmail.com"
        user['password'] = f"password{random.randint(1, 999999999)}"
        user['name'] = f"name{random.randint(1, 999999999)}"
        response = requests.post(paths.REGISTER_URL, data=user)
        actual_result = response.json()
                
        assert 200 == response.status_code
        assert True == actual_result['success']
        
        token = actual_result['accessToken']
        requests.delete(paths.USER_URL, headers={'authorization': token})


    required_fields = [{
            "email": "", 
            "password": "12345", 
            "name": "test"
        }, {
            "email": "test@gmail.com", 
            "password": "", 
            "name": "test"
        }, {
            "email": "test@gmail.com", 
            "password": "12345", 
            "name": ""
        }]
    @allure.title('Проверка отправки запроса без обязательных полей')
    @pytest.mark.parametrize('required_fields', required_fields)  
    def test_create_user_without_required_fields_negative_result(self, required_fields):
        response = requests.post(paths.REGISTER_URL, data=required_fields)
                
        assert 403 == response.status_code
        assert {"success":False, "message":messages.create_required_fields} == response.json()

    @allure.title('Проверка отправки запроса с существующим логином')    
    def test_create_repeat_user_already_used_result(self):
        user = {}
        user['email'] = f"user{random.randint(1, 999999999)}@gmail.com"
        user['password'] = f"password{random.randint(1, 999999999)}"
        user['name'] = f"name{random.randint(1, 999999999)}"
        response = requests.post(paths.REGISTER_URL, data=user)
        r = response.json()
        token = r['accessToken']
        response_repeat = requests.post(paths.REGISTER_URL, data=user)
                
        assert 403 == response_repeat.status_code
        assert {"success":False, "message":messages.user_already_exists} == response_repeat.json()

        requests.delete(paths.USER_URL, headers={'authorization': token})
