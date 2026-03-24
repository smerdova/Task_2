import random

class RequestHelper:
    @staticmethod
    def create_user_request(email = None, password = None, name = None):
        user = {}
        user['email'] = email or f"user{random.randint(1, 999999999)}@gmail.com"
        user['password'] = password or f"password{random.randint(1, 999999999)}"
        user['name'] = name or f"name{random.randint(1, 999999999)}"
        
        return user
    
    @staticmethod
    def login_user_request(email, password):
        login = {}
        login['email'] = email
        login['password'] = password

        return login
    
    @staticmethod
    def create_order_request(ingredients):
        payload = {
            "ingredients": ingredients
            }
    
        return payload
    
    @staticmethod
    def change_user_request(email = None, name = None):
        change_user_data = {
            "name": name or f"name{random.randint(1, 999999999)}",
            "email": email or f"email{random.randint(1, 999999999)}@gmail.com"
            }
        
        return change_user_data
