from typing import Any, Mapping

from ..base_repository import BaseRepository
from models import Family


class FamilyRepository(BaseRepository[Family]):
    table_name = "families"

    def _to_model(self, row: Mapping[str, Any]) -> Family:
        return Family(**dict(row))