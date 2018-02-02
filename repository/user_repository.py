import sys,os
sys.path.append(os.pardir)
from model.user import User
from data_store.users_store import UsersStore

class UserRepository:
    def add_user(self, user):
        UsersStore().add_user(user)
