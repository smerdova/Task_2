import random
import pytest
import paths as paths
import requests
from request_helper import RequestHelper

@pytest.fixture
def registered_user():
    user = RequestHelper.create_user_request()
    response_register = requests.post(paths.REGISTER_URL, data=user)
    r = response_register.json()
    user['accessToken'] = r['accessToken']

    yield user

    requests.delete(paths.USER_URL, headers={'authorization': user['accessToken']})

@pytest.fixture
def loggedin_user(registered_user):
    login = RequestHelper.login_user_request(registered_user['email'], registered_user['password'])
    response_login = requests.post(paths.LOGIN_URL, data=login)
    r = response_login.json()
    registered_user['accessToken'] = r['accessToken']
    
    return registered_user
