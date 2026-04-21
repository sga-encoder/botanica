from typing import Any, Mapping

from ..base_repository import BaseRepository
from models import Species


class SpeciesRepository(BaseRepository[Species]):
    table_name = "species"

    def _to_model(self, row: Mapping[str, Any]) -> Species:
        return Species(**dict(row))