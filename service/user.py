from dao.user import UserDAO
from utils import get_hash


class UserService:
    def __init__(self, dao: UserDAO):
        self.dao = dao

    def get_one(self, bid):
        return self.dao.get_one(bid)

    def get_all(self):
        return self.dao.get_all()

    def create(self, user_d):
        user_d['password'] = get_hash(user_d['password'])
        return self.dao.create(user_d)

    def delete(self, uid):
        self.dao.delete(uid)

    def patch(self, data):
        user = self.get_one(data['id'])

        if data.get('name'):
            user.name = data['name']
        if data.get('surname'):
            user.surname = data['surname']

    def update_password(self, data):
        pass

