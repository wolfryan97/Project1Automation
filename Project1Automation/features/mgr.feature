Feature: User(Manager) is able to interact with the manager tools

  Scenario Outline: Login to the application and get to the manager tools
    Given The User is on the login page
    When The User enters <username> into the username field
    When The User enters <password> into the password field
    When The User clicks on the login button
    Then The title should be <title>
    When The User clicks on the Manager Tools button
    Then The title should be Manager Tools Page

    Examples:
      | username | password | title |
      | user | pass | Employee Page |


  Scenario Outline: The Manager is able to accept a request, and deny a request
    Given The User is on the manager tools page
    When The User enters manager comment <mgr_comment> into the manager comment textarea <area>
    When The User clicks the button <button>
    Then An alert box should say <alert>
    When The User clicks the alert 'OK' button
    Then The title should be <title>

    Examples:
      | mgr_comment | area | button | alert | title |
      | Approved    | mgrCommentInput7 | accept7 | Request accepted. | Manager Tools Page |
      | No. You stink! | mgrCommentInput8 | deny8 | Request denied. | Manager Tools Page |
      | Sure thing, buddy | mgrCommentInput10 | accept10 | Request accepted. | Manager Tools Page |
      | Nope. | mgrCommentInput11 | deny11 | Request denied. | Manager Tools Page |


    Scenario Outline: The Manager is able to go back and see the resolved reimbursement requests
      Given The User is on the manager tools page
      When The User clicks the back button
      Then The title should be <title>
      Then The resolved table's size should be <size>

      Examples:
        | title | size |
        | Employee Page | 2 |

    Scenario Outline: The User(Employee) is able to see the resolved reimbursement requests
      Given The User is on the login page
      When The User enters <username> into the username field
      When The User enters <password> into the password field
      When The User clicks on the login button
      Then The title should be <title>
      Then The resolved table's size should be <size>

      Examples:
        | username | password | title | size |
        | user1 | pass2| Employee Page | 3 |

    Scenario Outline: The User(Manager) is able to view the statistics page
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

    Scenario: The User is able to logout
      Given The User is on the manager tools page
      When The User clicks the logout button
      Then Then The title should be Login Page
