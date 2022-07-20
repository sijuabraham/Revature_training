Feature: Login

#  Scenario: Successful login as student
#    Given that I am at the login page
#    When I type a valid username for a student
#    And a valid password for the student
#    And I click login
#    Then I should be redirected to the student

  Scenario Outline: Successful Login
    Given  that I am at the login page
    When I type in a valid username of <un>
    And a valid password of <pw>
    And  I click login
    Then I should be redirected to the <pagename> homepage

    Examples: Student credentials
    |un         | pw            |  pagename |
    | john_doe  | password12345 |student    |
    | jane_doe  | pass123       |student    |
    |bachy21    | password123   | teacher   |


#   This is an example of "data-driven" testing, whereby we parameterize our data for the test cases