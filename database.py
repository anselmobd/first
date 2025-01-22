from pprint import pprint


class Users():
    def __init__(self):
        self.__table = []
    
    def add_user(self, user):
        self.__table.append(user)

    def pprint(self):
        pprint(self.__table)
        