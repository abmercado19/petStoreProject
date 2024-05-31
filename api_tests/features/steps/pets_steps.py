import json
import logging
import os
import requests
from behave import *
from steps_utils import categories_mapping, tags_mapping

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)


@given("the valid endpoint to get a pet")
def define_endpoint_to_get_a_pet(context):
    """
    :param context: behave.runner.Context
    """
    context.get_pet_by_id_endpoint = os.path.join(context.base_url, "pet/{}")


@when("I retrieve the pet with id {pet_id}")
def retrieve_pet_with_specific_id(context, pet_id):
    """
    :param context: behave.runner.Context
    :param pet_id:
    """
    context.response = requests.get(context.get_pet_by_id_endpoint.format(pet_id))


@step("the response contains the pet data")
def verify_pet_data_is_displayed(context):
    """
    :param context: behave.runner.Context
    """
    response_data = context.response.json()
    assert 'id' in response_data, "Id is not retrieved in the response: {}".format(response_data)
    assert 'name' in response_data, "Name is not retrieved in the response: {}".format(response_data)
    assert 'category' in response_data, "Category is not retrieved in the response: {}".format(response_data)
    assert 'photoUrls' in response_data, "PhotoUrls is not retrieved in the response: {}".format(response_data)
    assert 'tags' in response_data, "Tags is not retrieved in the response: {}".format(response_data)
    assert 'status' in response_data, "Status is not retrieved in the response: {}".format(response_data)

    logging.info("Pet information was retrieved successfully")


@given("the valid endpoint to create a pet")
def define_endpoint_to_create_a_pet(context):
    """
    :param context: behave.runner.Context
    """
    context.create_pet_endpoint = os.path.join(context.base_url, "pet/")


@when("I create a pet with the following data")
def create_pet(context):
    """
    :type context: behave.runner.Context
    """
    table_data = context.table
    for row in table_data:
        context.pet_id = row['id']
        context.pet_name = row['name']
        context.pet_category_name = row['category']
        context.pet_category_id = categories_mapping[context.pet_category_name]
        context.pet_status = row['status']
        context.pet_photo_urls = row['photoUrls'].split(',')
        pet_tags_in_table = row['tags'].split(',')
        context.pet_tags = []
        for tag in pet_tags_in_table:
            context.pet_tags.append({"id": tags_mapping[tag], "name": tag})
        data = {"id": context.pet_id,
                "name": context.pet_name,
                "category": {"id": context.pet_category_id, "name": context.pet_category_name},
                "photoUrls": context.pet_photo_urls,
                "tags": context.pet_tags,
                "status": context.pet_status
                }
        context.response = requests.post(context.create_pet_endpoint, json=data)


@step("the pet data in the response matches with the added pet data")
def verify_pet_data_matches_with_data_added(context):
    """
    :param context: behave.runner.Context
    """
    response_data = context.response.json()
    assert str(response_data['id']) == str(context.pet_id), (
        "Id in response is '{}' and it is not matching with the added pet id {}".format(response_data['id'],
                                                                                        context.pet_id))
    assert response_data['name'] == context.pet_name, (
        "Name in response is {} and it is not matching with the added pet name {}".format(response_data['name'],
                                                                                          context.pet_name))
    assert response_data['category']['id'] == context.pet_category_id, \
        ("Category id in response is {} and it is not matching with the added category "
         "id {}").format(response_data['category']['id'], context.pet_category_id)
    assert response_data['category']['name'] == context.pet_category_name, \
        ("Category name in response is {} and it is not matching with the added category "
         "name {}").format(response_data['category']['name'], context.pet_category_name)
    assert response_data['photoUrls'] == context.pet_photo_urls, \
        ("PhotoUrls in response are {} and they are not matching with the "
         "added photoUrls {}").format(response_data['photoUrls'], context.pet_photo_urls)
    assert response_data['tags'] == context.pet_tags, \
        "Tags in response are {} and they are not matching with the added tags {}".format(response_data['tags'],
                                                                                          context.pet_tags)
    assert response_data['status'] == context.pet_status, \
        "Status in response is {} and it is not matching with the added status {}".format(response_data['status'],
                                                                                          context.pet_status)
