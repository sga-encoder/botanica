from models import Evaluation
from ...repositories import EvaluationRepository
from ..base_service import BaseRepositoryService


class EvaluationService(BaseRepositoryService[Evaluation]):
    def __init__(self):
        super().__init__(EvaluationRepository())
