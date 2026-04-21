from typing import Any, Mapping

from ..base_repository import BaseRepository
from models import Document


class DocumentRepository(BaseRepository[Document]):
    table_name = "documents"

    def _to_model(self, row: Mapping[str, Any]) -> Document:
        return Document(**dict(row))