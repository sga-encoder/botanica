from __future__ import annotations

import unittest
from typing import Any, cast

from models import User
from domain import UserService


class FakeUserRepository:
    def find_by_id(self, record_id):
        return User(id=str(record_id), name="Ada", email="ada@example.com", id_role="2")

    def find_one(self, filters):
        return None

    def find_many(self, filters=None, limit=None):
        return []

    def create(self, data):
        return data

    def update(self, data, filters):
        return [data]

    def delete(self, filters):
        return []


class UserServiceTests(unittest.TestCase):
    def test_get_user_info_returns_dict(self):
        service = UserService.__new__(UserService)
        service.repo = cast(Any, FakeUserRepository())

        data = service.get_user_info(7)
        
        assert data is not None

        self.assertEqual(data["id"], "7")
        self.assertEqual(data["name"], "Ada")


if __name__ == "__main__":
    unittest.main()