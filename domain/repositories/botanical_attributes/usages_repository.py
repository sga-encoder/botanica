from typing import Any, Mapping

from ..base_repository import BaseRepository
from models import Usages


class UsagesRepository(BaseRepository[Usages]):
    table_name = "usages"

    def _to_model(self, row: Mapping[str, Any]) -> Usages:
        return Usages(**dict(row))