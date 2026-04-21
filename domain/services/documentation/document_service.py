from models import Document
from ...repositories import DocumentRepository
from ..base_service import BaseRepositoryService


class DocumentService(BaseRepositoryService[Document]):
    def __init__(self):
        super().__init__(DocumentRepository())
