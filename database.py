from pprint import pprint
from model import User


class Users():
    def __init__(self):
        self._table = []
    
    def add_user(self, user):
        self._table.append(dict(user))

    def update_user(self, id, updated_user):
        for user in self._table:
            if user['id'] == id:
                user.update(dict(updated_user))
                return user

    def pprint(self):
        pprint(self._table)
