from typing import Any, Mapping

from ..base_repository import BaseRepository
from models import Role


class RoleRepository(BaseRepository[Role]):
    table_name = "roles"

    def _to_model(self, row: Mapping[str, Any]) -> Role:
        return Role(**dict(row))