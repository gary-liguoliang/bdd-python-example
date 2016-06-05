Feature: buy item
  as a customer, I want to get the item after I pay enough money.

  Scenario: customer buys an item with exact amount
    Given a working vending machine
      and "Coca-Cola" is available with price 1.20
    When I selected "Coca-Cola"
      and I pay 1.20
    Then I get a "Coca-Cola"


  Scenario: buy an item with exact amount
    Given a working vending machine
      and "Coca-Cola" is available with price 1.20
    When I selected "Coca-Cola"
      and I pay 1.19
    Then I get nothing