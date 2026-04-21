from models import Family
from ...repositories import FamilyRepository
from ..base_service import BaseRepositoryService


class FamilyService(BaseRepositoryService[Family]):
    def __init__(self):
        super().__init__(FamilyRepository())
