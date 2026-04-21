from __future__ import annotations

from typing import Any, Generic, TypeVar

from interfaces import RepositoryInterface, ServiceInterface

T = TypeVar("T")


class BaseRepositoryService(ServiceInterface[T], Generic[T]):
    def __init__(self, repository: RepositoryInterface[T]):
        self.repo = repository

    def get_by_id(self, record_id: int | str) -> T | None:
        return self.repo.find_by_id(record_id)

    def get_one(self, filters: dict[str, Any]) -> T | None:
        return self.repo.find_one(filters)

    def get_many(self, filters: dict[str, Any] | None = None, limit: int | None = None) -> list[T]:
        return self.repo.find_many(filters=filters, limit=limit)

    def create(self, data: dict[str, Any] | list[dict[str, Any]]) -> Any:
        return self.repo.create(data)

    def update(self, data: dict[str, Any], filters: dict[str, Any]) -> Any:
        return self.repo.update(data, filters)

    def delete(self, filters: dict[str, Any]) -> Any:
        return self.repo.delete(filters)
