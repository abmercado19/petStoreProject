import os
import requests
import logging
from behave import *


@given("the valid endpoint to place an order")
def define_endpoint_to_place_an_order(context):
    """
    :param context: behave.runner.Context
    """
    context.place_order_endpoint = os.path.join(context.base_url, "store/order")


@when("I create the order with the following data")
def create_order(context):
    """
    :param context: behave.runner.Context
    """
    table_data = context.table
    for row in table_data:
        context.order_id = row['id']
        context.pet_id = row['petId']
        context.order_quantity = row['quantity']
        context.order_ship_date = row['shipDate']
        context.order_status = row['status']
        context.order_complete = row['complete']
        data = {"id": context.order_id,
                "petId": context.pet_id,
                "quantity": context.order_quantity,
                "shipDate": context.order_ship_date,
                "status": context.order_status,
                "complete": context.order_complete
                }
        context.response = requests.post(context.place_order_endpoint, json=data)


@step("the response contains the order data")
def step_impl(context):
    """
    :param context: behave.runner.Context
    """
    response_data = context.response.json()
    assert 'id' in response_data, "id is not retrieved in the response: {}".format(response_data)
    assert 'petId' in response_data, "petId is not retrieved in the response: {}".format(response_data)
    assert 'quantity' in response_data, "quantity is not retrieved in the response: {}".format(response_data)
    assert 'status' in response_data, "status is not retrieved in the response: {}".format(response_data)
    assert 'complete' in response_data, "complete is not retrieved in the response: {}".format(response_data)

    logging.info("Order information was retrieved successfully")


@step("the order data in the response matches with the added order data")
def verify_order_data_matches_with_data_added(context):
    """
    :param context: behave.runner.Context
    """
    response_data = context.response.json()
    assert str(response_data['id']) == str(context.order_id), (
        "Id in response is '{}' and it is not matching with the added order id {}".format(response_data['id'],
                                                                                          context.order_id))
    assert str(response_data['petId']) == str(context.pet_id), (
        "Pet id in response is {} and it is not matching with the added pet id {}".format(response_data['petId'],
                                                                                          context.pet_id))
    assert str(response_data['quantity']) == str(context.order_quantity), \
        "Quantity in response is {} and it is not matching with the " \
        "added quantity {}".format(response_data['quantity'], context.order_quantity)
    assert response_data['status'] == context.order_status, \
        "Status in response is {} and it is not matching with the added status {}".format(response_data['status'],
                                                                                          context.order_status)
    assert str(response_data['complete']).lower() == str(context.order_complete).lower(), \
        "Complete in response is {} and it is not matching with the added " \
        "complete {}".format(response_data['complete'], context.order_complete)
