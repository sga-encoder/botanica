from typing import Any, Mapping

from ..base_repository import BaseRepository
from models import EmbeddingText


class EmbeddingTextRepository(BaseRepository[EmbeddingText]):
    table_name = "embedding_texts"

    def _to_model(self, row: Mapping[str, Any]) -> EmbeddingText:
        return EmbeddingText(**dict(row))