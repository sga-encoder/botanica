from models.vector_tables.image import Image
from ...repositories import ImageRepository
from ..base_service import BaseRepositoryService


class ImageService(BaseRepositoryService[Image]):
    def __init__(self):
        super().__init__(ImageRepository())
