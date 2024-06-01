# Created by anita at 31/05/2024
Feature: Pets management
  # This feature is going to be used for all the tests related to pets management (creation, edition, deletion, etc)

  @PET
  Scenario: Get a pet by an existent id
    When I retrieve the pet with id 5
    Then the response status code is 200
    And the response contains the pet data

  @PET
  Scenario: Get a pet by a non-existent id
    When I retrieve the pet with id 150
    Then the response status code is 404
    And the response contains the message "Pet not found"

  @PET
  Scenario: Create a pet with a non-existent id
    When I create a pet with the following data
    |id | name   | status    | category | photoUrls   | tags      |
    |53 | pomelo | available | Dogs     | url1,url2   | tag1,tag2 |
    Then the response status code is 200
    And the response contains the pet data
    And the pet data in the response matches with the added pet data

  @PET
  Scenario: Update an existent pet
    Given I create a pet with the following data
    |id | name   | status    | category | photoUrls   | tags      |
    |54 | pomelo | available | Dogs     | url1,url2   | tag1,tag2 |
    When I update the following data in the pet
    |id | name   | status    | category | photoUrls   | tags      |
    |83 | pomelo | sold      | Dogs     | url1,url2   | tag1,tag2 |
    Then the response status code is 200
    And the response contains the pet data
    And the pet data in the response matches with the updated pet data



