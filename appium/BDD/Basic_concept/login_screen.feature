Feature:fill the contact form

  Scenario:user login credentials

    Given Launch the app and click on login button
    When enter userid
    When password
    When  click on login button
    And opens home page
    Then verify home page
    Then take screenshot

    Scenario: Enter the data in Contact Form

        Given Launch the App and Click on ContactForm
        When Enter Name
        When Enter Email
        When Enter Mobile Number
        And we need to click on submit button
        Then Click on submit
        Then Take Screenshot of contact Form

