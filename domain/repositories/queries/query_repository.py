from typing import Any, Mapping

from ..base_repository import BaseRepository
from models import Query


class QueryRepository(BaseRepository[Query]):
    table_name = "queries"

    def _to_model(self, row: Mapping[str, Any]) -> Query:
        return Query(**dict(row))