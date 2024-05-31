from steps_utils import get_config
import json
import os
import logging
from behave import *
import requests


@given("the valid endpoint to login")
def define_endpoint_to_login(context):
    """
    :param context: behave.runner.Context
    """
    context.login_endpoint = os.path.join(context.base_url, "user/login")


@when("I login with a valid user and password")
def login_with_valid_data(context):
    """
    :param context: behave.runner.Context
    """
    config = get_config()
    user_name = config['valid_user']['user_name']
    password = config['valid_user']['password']
    data = {'user_name': user_name, 'password': password}
    context.response = requests.get(context.login_endpoint, data=json.dumps(data))


@step("the response contains the user session")
def verify_user_session_created(context):
    """
    :param context: behave.runner.Context
    """
    response_text= str(context.response.text)
    assert 'logged in user session:' in response_text.lower(), "Session is not retrieved in the response"
    session = response_text.replace('Logged in user session: ', '')
    assert int(session) > 0, "Session is not valid"
    logging.info("Session is retrieved in the response as expected")


@when("I login with an invalid user and password")
def login_with_invalid_user_and_password(context):
    """
    :param context: behave.runner.Context
    """
    config = get_config()
    user_name = config['invalid_user']['user_name']
    password = config['invalid_user']['password']
    data = {'user_name': user_name, 'password': password}
    context.response = requests.get(context.login_endpoint, data=json.dumps(data))
