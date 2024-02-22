Feature: Login

  Scenario: successful login
    Given create class objects
     When the user logs in with username "standard_user" and password "secret_sauce"
     Then login successful

#  Scenario: successful logout
#    Given the home page is open
#     When the user logs in with username "tomsmith" and password "SuperSecretPassword!"
#      And the user logs out
#     Then the message "You logged out of the secure area!" is shown


