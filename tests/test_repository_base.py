from __future__ import annotations

import unittest
from typing import Any, cast

from models import User
from domain import BaseRepository


class FakeDBAdapter:
    def __init__(self):
        self.calls = []

    def find_one(self, table, filters=None):
        self.calls.append(("find_one", table, filters))
        return {"id": "1", "name": "Ada", "email": "ada@example.com", "id_role": "2"}

    def find_many(self, table, filters=None, limit=None):
        self.calls.append(("find_many", table, filters, limit))
        return [
            {"id": "1", "name": "Ada", "email": "ada@example.com", "id_role": "2"},
            {"id": "2", "name": "Lin", "email": "lin@example.com", "id_role": "3"},
        ]

    def create(self, table, data):
        self.calls.append(("create", table, data))
        return data

    def update(self, table, data, filters):
        self.calls.append(("update", table, data, filters))
        return [data]

    def delete(self, table, filters):
        self.calls.append(("delete", table, filters))
        return [{"deleted": True}]


class UserRepositoryFake(BaseRepository[User]):
    table_name = "users"

    def _to_model(self, row):
        return User(**dict(row))


class AdapterRepositoryTests(unittest.TestCase):
    def setUp(self):
        self.db = FakeDBAdapter()
        self.repo = UserRepositoryFake(cast(Any, self.db))

    def test_find_by_id_maps_to_model(self):
        user = self.repo.find_by_id("1")

        assert user is not None
        self.assertIsInstance(user, User)
        self.assertEqual(user.name, "Ada")
        self.assertEqual(self.db.calls[0], ("find_one", "users", {"id": "1"}))

    def test_find_many_maps_each_row(self):
        users = self.repo.find_many(limit=2)

        self.assertEqual(len(users), 2)
        self.assertEqual(users[1].email, "lin@example.com")
        self.assertEqual(self.db.calls[0], ("find_many", "users", None, 2))

    def test_create_update_delete_delegate(self):
        self.repo.create({"name": "Ada"})
        self.repo.update({"name": "Ada Lovelace"}, {"id": 1})
        self.repo.delete({"id": 1})

        self.assertEqual(self.db.calls[0], ("create", "users", {"name": "Ada"}))
        self.assertEqual(self.db.calls[1], ("update", "users", {"name": "Ada Lovelace"}, {"id": 1}))
        self.assertEqual(self.db.calls[2], ("delete", "users", {"id": 1}))


if __name__ == "__main__":
    unittest.main()