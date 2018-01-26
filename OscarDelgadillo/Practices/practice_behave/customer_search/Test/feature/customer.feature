Feature: Customer search
  Simulate a search of a total priced for a list clients.


  Scenario Outline: Search a total price
    Given I have two list of clients and prices
    When I enter <Name> as name
      And I enter <ID> as ID
      And I enter <Price> as a total price
    Then the total price should be in the total price list

    Examples:
      | Name           | ID    | Price  |
      | Homero Simpson | ID001 | 123.4  |
      | March Simpson  | ID002 | 8450.4 |
      | Bart Simpson   | ID003 | 454.0  |
      | Lisa Simpson   | ID004 | 10.5   |


  Scenario: Search a client
    Given I have a list of clients
    When I enter Bart Simpson as name
    Then that name should be exist in the list of clients