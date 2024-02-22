#run:behave .\login_screen.feature --no-capture -f plain --tags functional
@functional
Feature:fill the contact form

  @smoke
  Scenario:user login credentials

    Given Launch the app and click on login button
    When enter userid
    When password
    When  click on login button
    And opens home page
    Then verify home page
    Then take screenshot

    @sanity
    Scenario: Enter the data in Contact Form

        Given Launch the App and Click on ContactForm
        When Enter Name
        When Enter Email
        When Enter Mobile Number
        And we need to click on submit button
        Then Click on submit
        Then Take Screenshot of contact Form

