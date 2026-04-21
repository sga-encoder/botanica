from typing import Any, Mapping

from ..base_repository import BaseRepository
from models import AltitudinalRange


class AltitudinalRangeRepository(BaseRepository[AltitudinalRange]):
    table_name = "altitudinal_ranges"

    def _to_model(self, row: Mapping[str, Any]) -> AltitudinalRange:
        return AltitudinalRange(**dict(row))