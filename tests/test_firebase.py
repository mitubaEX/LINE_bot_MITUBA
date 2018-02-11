from unittest import TestCase
from model.money import Money
from data_store.money_store import MoneyStore

class TestFirebase(TestCase):
    def test_get_money(self):
        moneyStore = MoneyStore()
        moneyStore.add_money(Money('0', 0))
        self.assertEqual(moneyStore.get_money(), 0)

