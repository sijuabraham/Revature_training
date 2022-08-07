Feature: login

  Scenario: Valid Login #1
    Given I am at the login page
    When I type in a valid username of "jane-doe"
    And I type in a valid password of "pass123"
    And I click the login button
    Then I should be redirected to the success page

  Scenario: Valid Login #2
    Given I am at the login page
    When I type in a valid username of "jane-doe"
    And I type in a valid password of "pass123"
    And I click the login button
    Then I should be redirected to the success page