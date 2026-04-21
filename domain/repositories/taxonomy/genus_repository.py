from typing import Any, Mapping

from ..base_repository import BaseRepository
from models import Genus


class GenusRepository(BaseRepository[Genus]):
    table_name = "genus"

    def _to_model(self, row: Mapping[str, Any]) -> Genus:
        return Genus(**dict(row))