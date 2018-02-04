import sys,os
sys.path.append(os.pardir)
from data_store.money_store import MoneyStore

class MoneyRepository:
    def add_money(self, money):
        MoneyStore().add_money(money)

    def get_money(self):
        return MoneyStore().get_money()
