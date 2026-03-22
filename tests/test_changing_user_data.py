import random
import allure
import pytest
import requests
import paths as paths
import messages as messages

class TestChangingUserData:
    change_user_data = [{
            "name": f"name{random.randint(1, 999999999)}",
            "email": f"email{random.randint(1, 999999999)}@gmail.com"
        }, {
            "name": f"name{random.randint(1, 999999999)}"
        }, {
            "email": f"email{random.randint(1, 999999999)}@gmail.com"
        }]

    @allure.title('Проверка успешного изменения учетной записи пользователя с авторизацией')
    @pytest.mark.parametrize('change_user_data', change_user_data)
    def test_changing_user_data_with_auth_positive_result(self, user_register, change_user_data):
        response_change_user = requests.patch(paths.USER_URL, data=change_user_data, headers={'authorization': user_register['accessToken']})
        actual_result = response_change_user.json()
                
        assert 200 == response_change_user.status_code
        assert True == actual_result['success']

    @allure.title('Проверка невозможности изменения учетной записи пользователя без авторизациеи')
    def test_changing_user_data_without_auth_negative_result(self):
        change_user_data = {
            "name": f"name{random.randint(1, 999999999)}",
            "email": f"email{random.randint(1, 999999999)}@gmail.com"
            }
        response_change_user = requests.patch(paths.USER_URL, data=change_user_data)
                        
        assert 401 == response_change_user.status_code
        assert {"success":False, "message":messages.authorization_required} == response_change_user.json()
