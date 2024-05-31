# Created by anita at 31/05/2024
Feature: Users management
  # This feature is going to be used for all the tests related to users management (creation, edition, deletion, etc)

  Scenario: Login with an existent user
    Given the valid endpoint to login
    When I login with a valid user and password
    Then the response status code is 200
    And the response contains the user session

  Scenario: Login with an invalid user and password
    Given the valid endpoint to login
    When I login with an invalid user and password
    Then the response status code is 400
