from decimal import Decimal

from lettuce import step, world
from vm.vending_machine import VendingMachine



@step(u'Given a working vending machine')
def given_a_working_vending_machine(step):
    world.vm = VendingMachine()
    # assert False, 'This step must be implemented'


@step(u'and "([^"]*)" is available with price (.+)')
def setup_inventory(step, item_name, price):
    world.vm.add_to_inventory(item_name, Decimal(price))


@step(u'When I selected "([^"]*)"')
def when_i_selected_group1(step, select_item):
    world.selected_item = select_item


@step(u'and I pay (.+)')
def and_i_pay_1_20(step, amout):
    world.paid_amount = Decimal(amout)


@step(u'Then I get a "([^"]*)"')
def then_i_get_a_group1(step, group1):
    item_received = world.vm.sell_item(world.selected_item, world.paid_amount)
    assert item_received.name == world.selected_item


@step("I get nothing")
def get_nothing(step):
    item_received = world.vm.sell_item(world.selected_item, world.paid_amount)
    assert not item_received