from models import Role
from ...repositories import RoleRepository
from ..base_service import BaseRepositoryService


class RoleService(BaseRepositoryService[Role]):
    def __init__(self):
        super().__init__(RoleRepository())
