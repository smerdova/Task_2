import allure
import requests
import paths as paths
import messages as messages
import test_data as test_data
from request_helper import RequestHelper

class TestGetOrderSpecificUser:
    @allure.title('Проверка получения списка заказов конкретного пользователя с авторизацией')
    @allure.step('Проверяем успешное получение списка заказов конкретного пользователя с авторизацией')
    def test_get_order_specific_user_with_auth_positive_result(self, loggedin_user):
        payload_ingredients = RequestHelper.create_order_request(test_data.hashs_ingredients)
        requests.post(paths.ORDER_URL, data=payload_ingredients, headers={'authorization': loggedin_user['accessToken']})
        response = requests.get(paths.ORDER_URL, headers={'authorization': loggedin_user['accessToken']})
        actual_result = response.json()
                
        assert 200 == response.status_code
        assert True == actual_result['success']

    @allure.title('Проверка получения списка заказов без авторизации')
    @allure.step('Проверяем, что невозможно получить список заказов без авторизации')
    def test_get_order_without_auth_negative_result(self):
        response = requests.get(paths.ORDER_URL)
                        
        assert 401 == response.status_code
        assert {"success":False, "message":messages.authorization_required} == response.json()
