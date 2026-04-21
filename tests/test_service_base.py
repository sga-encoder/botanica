from __future__ import annotations

import unittest

from typing import Any, cast

from models import User
from domain import BaseRepositoryService
from interfaces import RepositoryInterface


class FakeRepository:
    def __init__(self):
        self.calls = []

    def find_by_id(self, record_id):
        self.calls.append(("find_by_id", record_id))
        return User(id="1", name="Ada", email="ada@example.com", id_role="2")

    def find_one(self, filters):
        self.calls.append(("find_one", filters))
        return None

    def find_many(self, filters=None, limit=None):
        self.calls.append(("find_many", filters, limit))
        return [User(id="1", name="Ada", email="ada@example.com", id_role="2")]

    def create(self, data):
        self.calls.append(("create", data))
        return data

    def update(self, data, filters):
        self.calls.append(("update", data, filters))
        return [data]

    def delete(self, filters):
        self.calls.append(("delete", filters))
        return [{"deleted": True}]


class UserServiceLike(BaseRepositoryService[User]):
    pass


class RepositoryServiceTests(unittest.TestCase):
    def setUp(self):
        self.repository = FakeRepository()
        self.service = UserServiceLike(cast(RepositoryInterface[User], self.repository))

    def test_get_by_id_delegates(self):
        user = self.service.get_by_id(1)
        
        assert user is not None

        self.assertEqual(user.name, "Ada")
        self.assertEqual(self.repository.calls[0], ("find_by_id", 1))

    def test_get_many_delegates(self):
        users = self.service.get_many(limit=1)

        self.assertEqual(len(users), 1)
        self.assertEqual(self.repository.calls[0], ("find_many", None, 1))

    def test_mutations_delegate(self):
        self.service.create({"name": "Ada"})
        self.service.update({"name": "Ada Lovelace"}, {"id": 1})
        self.service.delete({"id": 1})

        self.assertEqual(self.repository.calls[0], ("create", {"name": "Ada"}))
        self.assertEqual(self.repository.calls[1], ("update", {"name": "Ada Lovelace"}, {"id": 1}))
        self.assertEqual(self.repository.calls[2], ("delete", {"id": 1}))


if __name__ == "__main__":
    unittest.main()