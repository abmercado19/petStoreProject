from behave import *
import logging


@then("the response status code is {response_code}")
def verify_response_status_code(context, response_code):
    """
    :param context: behave.runner.Context
    :param response_code: response code
    """
    assert context.response.status_code == int(response_code), \
        "Response code should be '{}' but it is '{}' \n Response content: {}".format(response_code,
                                                                                     context.response.status_code,
                                                                                     context.response.content)
    logging.info("Response code is '{}' as expected".format(response_code))


@step('the response contains the message "{error_message}"')
def step_impl(context, error_message):
    """
    :param context: behave.runner.Context
    :param error_message: error message
    """
    response_text = str(context.response.text)
    assert error_message.lower() in response_text.lower(), (
        "Error message '{}' is not in the response. Response: {}".format(error_message, response_text))
    logging.info("Error message '{}' is in the response as expected".format(error_message))

