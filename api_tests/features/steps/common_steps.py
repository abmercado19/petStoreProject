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

