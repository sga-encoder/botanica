from typing import Any, Mapping

from ..base_repository import BaseRepository
from models import Session


class SessionRepository(BaseRepository[Session]):
    table_name = "sessions"

    def _to_model(self, row: Mapping[str, Any]) -> Session:
        return Session(**dict(row))