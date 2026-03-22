import random
import pytest
import paths as paths
import requests

@pytest.fixture
def user_register():
    user_register = {}
    user_register['email'] = f"email{random.randint(1, 999999999)}@gmail.com"
    user_register['password'] = f"password{random.randint(1, 999999999)}"
    user_register['name'] = f"name{random.randint(1, 999999999)}"
    response_register = requests.post(paths.REGISTER_URL, data=user_register)
    r = response_register.json()
    user_register['accessToken'] = r['accessToken']

    yield user_register

    requests.delete(paths.USER_URL, headers={'authorization': user_register['accessToken']})

@pytest.fixture
def user():
    user = {}
    user['email'] = f"email{random.randint(1, 999999999)}@gmail.com"
    user['password'] = f"password{random.randint(1, 999999999)}"
    user['name'] = f"name{random.randint(1, 999999999)}"
    requests.post(paths.REGISTER_URL, data=user)
    login = {}
    login['email'] = user['email']
    login['password'] = user['password']
    response_login = requests.post(paths.LOGIN_URL, data=login)
    r = response_login.json()
    user['accessToken'] = r['accessToken']
    
    yield user

    requests.delete(paths.USER_URL, headers={'authorization': user['accessToken']})
