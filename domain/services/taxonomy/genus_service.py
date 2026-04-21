from models import Genus
from ...repositories import GenusRepository
from ..base_service import BaseRepositoryService


class GenusService(BaseRepositoryService[Genus]):
    def __init__(self):
        super().__init__(GenusRepository())
