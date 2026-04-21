from typing import Any, Mapping

from ..base_repository import BaseRepository
from models import Evaluation


class EvaluationRepository(BaseRepository[Evaluation]):
    table_name = "evaluations"

    def _to_model(self, row: Mapping[str, Any]) -> Evaluation:
        return Evaluation(**dict(row))