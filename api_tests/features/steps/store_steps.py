import logging
from behave import *

from api_tests.features.steps.endpoints.store_endpoints import StoreEndpoints


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
        store_endpoint = StoreEndpoints()
        context.response = store_endpoint.create_order(context.order_id, context.pet_id, context.order_quantity,
                                                       context.order_ship_date, context.order_status,
                                                       context.order_complete)


@step("the response contains the order data")
def verify_order_data_is_displayed(context):
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


@when("I retrieve the order with the id {order_id}")
def retrieve_order_with_specific_id(context, order_id):
    """
    :param context: behave.runner.Context
    :param order_id: order id
    """
    store_endpoint = StoreEndpoints()
    context.response = store_endpoint.get_order_by_id(order_id)
