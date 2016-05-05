from lettuce import step, world
from vm.vending_machine import VendingMachine


@step(u'Given "([^"]*)" is available in the vending machine and the price is 1.20')
def given_group1_is_available_in_the_vending_machine_and_the_price_is_1_20(step, group1):
    world.items = []
    world.items.append(group1)


@step(u'Given I selected "([^"]*)"')
def given_i_selected_100(step, item):
    world.selected = item


@step(u'When I pay (.+)')
def when_i_pay_1_20(step,  amount):
    print amount


@step(u'Then I get a "([^"]*)"')
def then_i_get_1_group1(step, group1):
    print '\n items: %s, selected: %s' % (world.items,  world.selected)
    print VendingMachine()
    # assert False, 'This step must be implemented'