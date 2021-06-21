Feature: User(Manager) is able to view statistics

  Scenario Outline: Login to the application and get to the statistics
    Given The User is on the login page
    When The User enters <username> into the username field
    When The User enters <password> into the password field
    When The User clicks on the login button
    Then The title should be <title>
    When The User clicks on the Manager Tools button
    Then The title should be Manager Tools Page
    When The User clicks on the View Statistics button
    Then The title should be Statistics Page

    Examples:
        | username | password | title |
        | user     | pass     | Employee Page |

  Scenario: The User(Manager) is able to view statistics
    Given The User is on the statistics page
    Then The Pie Chart exists
    Then The Vertical Bar Graph exists

  Scenario Outline: The User(Manager) is able to both go back from the statistics page and logout
    Given The User is on the statistics page
    When The User clicks the back button
    Then The title should be <title>
    When The User clicks on the View Statistics button
    Then The title should be Statistics Page
    When The User clicks the logout button
    Then Then The title should be Login Page
    Examples:
      | title |
      | Manager Tools Page |