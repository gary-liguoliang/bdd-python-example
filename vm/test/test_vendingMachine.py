from unittest import TestCase

from vm.vending_machine import VendingMachine


class TestVendingMachine(TestCase):

    def setUp(self):
        super(TestVendingMachine, self).setUp()
        self.vending_machine = VendingMachine()

    def test_sell_item(self):
        item_name = "Coca"
        self.vending_machine.add_to_inventory(item_name, 1.0)
        item_received = self.vending_machine.sell_item("%s" % item_name, 1.0)
        self.assertIsNotNone(item_received)
