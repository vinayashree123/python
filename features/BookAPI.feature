#run command - behave features/BookAPI.feature  --no-capture
# tagging command - behave features/BookAPI.feature  --no-capture --tags=smoke
Feature:verify if books are added and deleted into Library successfully.

  #Tagging
  @smoke
  Scenario:verify AddBook API functionality
    Given the book details which need to add into library
    When execute AddBook post API method
    Then the book is successfully added


  #parameterized - when you want to run same scenarios with multile data then use scenario_outline
  @regression
  Scenario Outline: :verify AddBook API functionality
    Given the book details with <isbn> and <aisle>
    When execute AddBook post API method
    Then the book is successfully added
    Examples:
      | isbn |  aisle |
      | B101 | 227    |
      | B102 | 227    |




