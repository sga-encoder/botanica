from typing import Any, Mapping

from ..base_repository import BaseRepository
from models import User


class UserRepository(BaseRepository[User]):
    table_name = "users"

    def _to_model(self, row: Mapping[str, Any]) -> User:
        return User(**dict(row))
