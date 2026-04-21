from models import User
from ...repositories import UserRepository
from ..base_service import BaseRepositoryService


class UserService(BaseRepositoryService[User]):
    def __init__(self):
        super().__init__(UserRepository())

    def get_user_info(self, user_id: int) -> dict | None:
        user: User | None = self.get_by_id(user_id)
        if user:
            return user.model_dump()
        return None
