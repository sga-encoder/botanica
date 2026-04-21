from models import Session
from ...repositories import SessionRepository
from ..base_service import BaseRepositoryService


class SessionService(BaseRepositoryService[Session]):
    def __init__(self):
        super().__init__(SessionRepository())
