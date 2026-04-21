from models import Species
from ...repositories import SpeciesRepository
from ..base_service import BaseRepositoryService


class SpeciesService(BaseRepositoryService[Species]):
    def __init__(self):
        super().__init__(SpeciesRepository())
