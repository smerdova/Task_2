import allure
import requests
import paths as paths
import messages as messages
from request_helper import RequestHelper
import test_data as test_data

class TestCreateOrder:
    @allure.title('Проверка создания заказа без авторизации с ингредиентами')
    @allure.step('Проверяем успешное создание заказа без авторизации с ингредиентами')
    def test_create_order_without_auth_with_ingredients_positive_result(self):
        payload = RequestHelper.create_order_request(test_data.hashs_ingredients)
        response = requests.post(paths.ORDER_URL, data=payload)
        actual_result = response.json()
                
        assert 200 == response.status_code
        assert True == actual_result['success']

    @allure.title('Проверка создания заказа без авторизации без ингредиентов')
    @allure.step('Проверяем, что заказ не создается без авторизации и без ингредиентов')
    def test_create_order_without_auth_without_ingredients_negative_result(self):
        payload = RequestHelper.create_order_request([])
        response = requests.post(paths.ORDER_URL, data=payload)
                        
        assert 400 == response.status_code
        assert {"success":False, "message":messages.ingredient_ids_required} == response.json()

    @allure.title('Проверка создания заказа без авторизации с неверным хешем ингредиентов')
    @allure.step('Проверяем, что заказ не создается без авторизации с неверным хешем ингредиентов')
    def test_create_order_without_auth_with_incorrect_hash_negative_result(self):
        payload = RequestHelper.create_order_request(["12345"])
        response = requests.post(paths.ORDER_URL, data=payload)
                        
        assert 500 == response.status_code

    @allure.title('Проверка создания заказа с авторизацией с ингредиентами')
    @allure.step('Проверяем успешное создание заказа с авторизацей и с ингредиентами')
    def test_create_order_with_auth_with_ingredients_positive_result(self, loggedin_user):
        payload = RequestHelper.create_order_request(test_data.hashs_ingredients)
        response_order = requests.post(paths.ORDER_URL, data=payload, headers={'authorization': loggedin_user['accessToken']})
        actual_result = response_order.json()
                
        assert 200 == response_order.status_code
        assert True == actual_result['success']

    @allure.title('Проверка создания заказа с авторизацией без ингредиентов')
    @allure.step('Проверяем, что заказ не создается с авторизацией и без ингредиентов')
    def test_create_order_with_auth_without_ingredients_negative_result(self, loggedin_user):              
        payload = RequestHelper.create_order_request([])
        response_order = requests.post(paths.ORDER_URL, data=payload, headers={'authorization': loggedin_user['accessToken']})
                        
        assert 400 == response_order.status_code
        assert {"success":False, "message":messages.ingredient_ids_required} == response_order.json()

    @allure.title('Проверка создания заказа с авторизацией с неверным хешем ингредиентов')
    @allure.step('Проверяем, что заказ не создается с авторизацией и с неверным хешем ингредиентов')
    def test_create_order_with_auth_with_incorrect_hash_negative_result(self, loggedin_user):           
        payload = RequestHelper.create_order_request(["12345"])
        response_order = requests.post(paths.ORDER_URL, data=payload, headers={'authorization': loggedin_user['accessToken']})

        assert 500 == response_order.status_code
