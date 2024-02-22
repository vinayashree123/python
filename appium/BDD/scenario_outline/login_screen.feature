Feature:fill the contact form

  Scenario Outline: :user login credentials

    Given Launch the app and click on login button
    When enter <userid> userid
    When password <password>
    When  click on login button
    And opens home page
    Then verify home page
    Then take screenshot

    Examples:
    | userid | password |
    | vina@gmail.com | 1234|
    | naganuri@gmail.com | 0001 |






