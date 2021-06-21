Feature: User is able to submit and view a reimbursement request

  Scenario Outline: Login to the employee reimbursement application as a manager
    Given The User is on the login page
    When The User enters <username> into the username field
    When The User enters <password> into the password field
    When The User clicks on the login button
    Then The title should be <title>

    Examples:
      | username | password | title |
      | user     | pass     | Employee Page |

  Scenario Outline: The User is unable to enter a negative number
    Given The User is on the employee page
    When The User enters an amount <amount>
    When The User enters a description <description>
    When The User clicks the submit button
    Then An alert box should say <alert>
    When The User clicks the alert 'OK' button
    Then The title should be <title>

    Examples:
      | amount | description | alert | title |
      | -100   | Negative test | Please enter a positive number for Amount. | Employee Page |

  Scenario: The User is able to logout
    Given The User is on the employee page
    When The User clicks the logout button
    Then Then The title should be Login Page


  Scenario Outline: Login to the employee reimbursement application as a manager
    Given The User is on the login page
    When The User enters <username> into the username field
    When The User enters <password> into the password field
    When The User clicks on the login button
    Then The title should be <title>

    Examples:
      | username | password | title |
      | user     | pass     | Employee Page |


  Scenario Outline: User(Manager) is able to submit 2 more requests
    Given The User is on the employee page
    When The User enters an amount <amount>
    When The User enters a description <description>
    When The User clicks the submit button
    Then An alert box should say <alert>
    When The User clicks the alert 'OK' button
    Then The pending table's size should be <size>

    Examples:
      | amount | description | size | alert |
      | 300 | Sponsor Lunch | 2     | The request was successfully added. |
      | 250 | Give me money pls | 3 | The request was successfully added. |

  Scenario Outline: User(Manager) request will fail if already 3 pending requests
    Given The User is on the employee page
    When The User enters an amount <amount>
    When The User enters a description <description>
    When The User clicks the submit button
    Then An alert box should say <alert>
    When The User clicks the alert 'OK' button
    Then The title should be <title>
    Then The amount textbox should be empty
    Then The description textarea should be empty

      Examples:
        | amount | description | alert | title |
        | 100 | Sponsor Lunch | No more than 3 requests allowed at a given time. | Employee Page |

  Scenario: User(Manager) will go to the manager tools page
    Given The User is on the employee page
    When The User clicks on the Manager Tools button
    Then The title should be Manager Tools Page


  Scenario Outline: Login to the employee reimbursement application as a regular employee
      Given The User is on the login page
      When The User enters <username> into the username field
      When The User enters <password> into the password field
      When The User clicks on the login button
      Then The title should be <title>

      Examples:
        | username | password | title |
        | user1     | pass2     | Employee Page |

  Scenario Outline: User(Employee) is able to submit 3 more requests
    Given The User is on the employee page
    When The User enters an amount <amount>
    When The User enters a description <description>
    When The User clicks the submit button
    Then An alert box should say <alert>
    When The User clicks the alert 'OK' button
    Then The pending table's size should be <size>

    Examples:
      | amount | description | size | alert |
      | 300 | I just need money | 1 | The request was successfully added. |
      | 180 | Hotel Expenses | 2    | The request was successfully added. |
      | 550 | Hotel Expenses    | 3 | The request was successfully added. |

  Scenario Outline: User(Employee) request will fail if already 3 pending requests
    Given The User is on the employee page
    When The User enters an amount <amount>
    When The User enters a description <description>
    When The User clicks the submit button
    Then An alert box should say <alert>
    When The User clicks the alert 'OK' button
    Then The title should be <title>
    Then The amount textbox should be empty
    Then The description textarea should be empty

    Examples:
        | amount | description | alert | title |
        | 500 | Sponsor Lunch | No more than 3 requests allowed at a given time. | Employee Page |

  Scenario Outline: User(Employee) is not able to go to the manager tools page
    Given The User is on the employee page
    When The User clicks on the Manager Tools button
    Then An alert box should say <alert>
    When The User clicks the alert 'OK' button
    Then The title should be <title>

    Examples:
      | alert | title |
      | You must be a manager for this feature. | Employee Page |
