# Created by anita at 31/05/2024
Feature: Pets management
  # This feature is going to be used for all the tests related to pets management (creation, edition, deletion, etc)

  Scenario: Get a pet by an existent id
    Given the valid endpoint to get a pet
    When I retrieve the pet with id 5
    Then the response status code is 200
    And the response contains the pet data

  Scenario: Create a pet with a non-existent id
    Given the valid endpoint to create a pet
    When I create a pet with the following data
    |id | name   | status    | category | photoUrls   | tags      |
    |53 | pomelo | available | Dogs     | url1,url2   | tag1,tag2 |
    Then the response status code is 200
    And the response contains the pet data
    And the pet data in the response matches with the added pet data
