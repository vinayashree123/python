*** Test Cases ***
Example Test Case
    ${fruits}    Create List    Apple    Banana    Orange    # Create a list variable containing fruits
    Log    ${fruits}    # Print the list variable to the console
    Log    Length of Fruits: ${fruits.__len__()}    # Get the length of the list variable
    Log    First Fruit: ${fruits[0]}    # Access the first item in the list
    Log    Last Fruit: ${fruits[-1]}    # Access the last item in the list
    FOR    ${fruit}    IN    @{fruits}    # Loop through the list and print each fruit
        Log    Fruit: ${fruit}
    END

*** Keywords ***
