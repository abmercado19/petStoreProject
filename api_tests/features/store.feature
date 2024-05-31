# Created by anita at 31/05/2024
Feature: Store transactions
  # This feature is going to be used for all the store transactions (add order, delete order, find order, etc)

  Scenario: Place a new order in the store
    Given the valid endpoint to place an order
    When I create the order with the following data
      | id | petId | quantity | shipDate            | status | complete |
      | 70 | 53    | 100      | 2024-05-31T12:00:00 | placed | true     |
    Then the response status code is 200
    And the response contains the order data
    And the order data in the response matches with the added order data