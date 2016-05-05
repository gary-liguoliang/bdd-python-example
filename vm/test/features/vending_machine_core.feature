Feature: buy item
  as a customer, I want to get the item after I pay enough money.

  Scenario: buy an item with exact amount
    Given "Coca-Cola" is available in the vending machine and the price is 1.20
    Given I selected "Coca-Cola"
    When I pay 1.20
    Then I get a "Coca-Cola""

