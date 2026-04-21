from models.vector_tables.embedding_text import EmbeddingText
from ...repositories import EmbeddingTextRepository
from ..base_service import BaseRepositoryService


class EmbeddingTextService(BaseRepositoryService[EmbeddingText]):
    def __init__(self):
        super().__init__(EmbeddingTextRepository())
