from models import Query
from ...repositories import QueryRepository
from ..base_service import BaseRepositoryService


class QueryService(BaseRepositoryService[Query]):
    def __init__(self):
        super().__init__(QueryRepository())
