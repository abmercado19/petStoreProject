# Created by anita at 31/05/2024
Feature: Store transactions
  # This feature is going to be used for all the store transactions (add order, delete order, find order, etc)

  @STORE
  Scenario: Place a new order in the store
    When I create the order with the following data
      | id | petId | quantity | shipDate            | status | complete |
      | 70 | 53    | 100      | 2024-05-31T12:00:00 | placed | true     |
    Then the response status code is 200
    And the response contains the order data
    And the order data in the response matches with the added order data

  @STORE
  Scenario: Get an order by an existent id
    When I retrieve the order with the id 70
    Then the response status code is 200
    And the response contains the order data

  @STORE
  Scenario: Get an order by an non-existent id
    When I retrieve the order with the id 6
    Then the response status code is 404
    And the response contains the message "Order not found"

  @STORE
  Scenario: Get an order by an invalid id
    When I retrieve the order with the id %
    Then the response status code is 400
    And the response contains the message "Invalid ID supplied"