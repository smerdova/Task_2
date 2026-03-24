import random

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
hashs_ingredients = ["61c0c5a71d1f82001bdaaa70", "61c0c5a71d1f82001bdaaa6d"]
change_user_data = [{
            "name": f"name{random.randint(1, 999999999)}",
            "email": f"email{random.randint(1, 999999999)}@gmail.com"
        }, {
            "name": f"name{random.randint(1, 999999999)}"
        }, {
            "email": f"email{random.randint(1, 999999999)}@gmail.com"
        }]
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
