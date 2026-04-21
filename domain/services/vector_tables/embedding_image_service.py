from models.vector_tables.embedding_image import EmbeddingImage
from ...repositories import EmbeddingImageRepository
from ..base_service import BaseRepositoryService


class EmbeddingImageService(BaseRepositoryService[EmbeddingImage]):
    def __init__(self):
        super().__init__(EmbeddingImageRepository())
