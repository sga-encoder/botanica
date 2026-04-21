from models import Usages
from ...repositories import UsagesRepository
from ..base_service import BaseRepositoryService


class UsagesService(BaseRepositoryService[Usages]):
    def __init__(self):
        super().__init__(UsagesRepository())
