from typing import Any, Mapping

from ..base_repository import BaseRepository
from models import EmbeddingImage


class EmbeddingImageRepository(BaseRepository[EmbeddingImage]):
    table_name = "embedding_images"

    def _to_model(self, row: Mapping[str, Any]) -> EmbeddingImage:
        return EmbeddingImage(**dict(row))