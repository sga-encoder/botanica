from models import Chunk
from ...repositories import ChunkRepository
from ..base_service import BaseRepositoryService


class ChunkService(BaseRepositoryService[Chunk]):
    def __init__(self):
        super().__init__(ChunkRepository())
