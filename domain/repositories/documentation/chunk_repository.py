from typing import Any, Mapping

from ..base_repository import BaseRepository
from models import Chunk


class ChunkRepository(BaseRepository[Chunk]):
    table_name = "chunks"

    def _to_model(self, row: Mapping[str, Any]) -> Chunk:
        return Chunk(**dict(row))