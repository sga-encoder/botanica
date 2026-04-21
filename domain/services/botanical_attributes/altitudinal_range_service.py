from models import AltitudinalRange
from ...repositories import AltitudinalRangeRepository
from ..base_service import BaseRepositoryService


class AltitudinalRangeService(BaseRepositoryService[AltitudinalRange]):
    def __init__(self):
        super().__init__(AltitudinalRangeRepository())
