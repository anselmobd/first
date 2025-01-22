from model import User
from database import Users

def test_add_user():
    user = User(
        id=1, name="Pi", email="pi@math", password="123")
    users_db = Users()

    users_db.add_user(user)

    assert len(users_db._table) == 1
    assert users_db._table[0]['id'] == 1
    assert users_db._table[0]['name'] == "Pi"
