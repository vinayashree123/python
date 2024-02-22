Feature:fill the contact form

  Scenario:user login credentials

    Given Launch the app and click on login button
    When enter 'vina@gmail.com' userid
    When password 1234
    When  click on login button
    And opens home page
    Then verify home page
    Then take screenshot



