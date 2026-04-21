from models import SpeciesUsages
from ...repositories import SpeciesUsagesRepository
from ..base_service import BaseRepositoryService


class SpeciesUsagesService(BaseRepositoryService[SpeciesUsages]):
    def __init__(self):
        super().__init__(SpeciesUsagesRepository())
