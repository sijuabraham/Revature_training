Feature: login


  Scenario: Valid Login
    Given I am at the login page
    When I type in a valid username of <username>
    And I type in a valid password of <password>
    And I click the login button
    Then I should be redirected to the success page

    Examples:
      | username| password |
      | "jane-doe" | "pass123" |
      | "jane-doe" | "pass123" |