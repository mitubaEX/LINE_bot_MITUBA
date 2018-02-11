import sys
import os
sys.path.append(os.pardir)
from data_store.money_store import MoneyStore


class MoneyRepository:
    def __init__(self):
        self.moneyStore = MoneyStore()

    def add_money(self, money):
        self.moneyStore.add_money(money)

    def get_money(self):
        return self.moneyStore.get_money()

    def decrease_money(self, money):
        money.money = self.moneyStore.get_money() - money.money
        self.moneyStore.add_money(money)
        return int(self.moneyStore.get_money())

    def increase_money(self, money):
        money.money = self.moneyStore.get_money() + money.money
        self.moneyStore.add_money(money)
        return int(self.moneyStore.get_money())
