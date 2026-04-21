from typing import Any, Mapping

from ..base_repository import BaseRepository
from models import Image


class ImageRepository(BaseRepository[Image]):
    table_name = "images"

    def _to_model(self, row: Mapping[str, Any]) -> Image:
        return Image(**dict(row))