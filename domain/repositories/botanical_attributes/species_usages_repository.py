from typing import Any, Mapping

from ..base_repository import BaseRepository
from models import SpeciesUsages


class SpeciesUsagesRepository(BaseRepository[SpeciesUsages]):
    table_name = "species_usages"

    def _to_model(self, row: Mapping[str, Any]) -> SpeciesUsages:
        return SpeciesUsages(**dict(row))