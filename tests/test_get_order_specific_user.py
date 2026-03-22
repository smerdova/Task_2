import allure
import requests
import paths as paths
import messages as messages

class TestGetOrderSpecificUser:
    @allure.title('Проверка получения списка заказов конкретного пользователя с авторизацией')
    def test_get_order_specific_user_with_auth_positive_result(self, user):
        payload_ingredients = {
            "ingredients": ["61c0c5a71d1f82001bdaaa70", "61c0c5a71d1f82001bdaaa6d"] 
            }
        requests.post(paths.ORDER_URL, data=payload_ingredients, headers={'authorization': user['accessToken']})
        response = requests.get(paths.ORDER_URL, headers={'authorization': user['accessToken']})
        actual_result = response.json()
                
        assert 200 == response.status_code
        assert True == actual_result['success']

    @allure.title('Проверка получения списка заказов без авторизации')
    def test_get_order_without_auth_negative_result(self):
        response = requests.get(paths.ORDER_URL)
                        
        assert 401 == response.status_code
        assert {"success":False, "message":messages.authorization_required} == response.json()
