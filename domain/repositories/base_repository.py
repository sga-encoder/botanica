from __future__ import annotations

from abc import ABC, abstractmethod
from typing import Any, Generic, Mapping, TypeVar

from adapters import DBAdapter
from interfaces import RepositoryInterface

T = TypeVar("T")


class BaseRepository(RepositoryInterface[T], ABC, Generic[T]):
    table_name: str

    def __init__(self, db_adapter: DBAdapter | None = None):
        self.db = db_adapter or DBAdapter()

    @abstractmethod
    def _to_model(self, row: Mapping[str, Any]) -> T:
        raise NotImplementedError

    def find_by_id(self, record_id: int | str) -> T | None:
        return self.find_one({"id": record_id})

    def find_one(self, filters: dict[str, Any]) -> T | None:
        data = self.db.find_one(self.table_name, filters=filters)
        if isinstance(data, Mapping):
            return self._to_model(data)
        return None

    def find_many(self, filters: dict[str, Any] | None = None, limit: int | None = None) -> list[T]:
        data = self.db.find_many(self.table_name, filters=filters, limit=limit)
        if not isinstance(data, list):
            return []
        return [self._to_model(row) for row in data if isinstance(row, Mapping)]

    def create(self, data: dict[str, Any] | list[dict[str, Any]]) -> Any:
        return self.db.create(self.table_name, data)

    def update(self, data: dict[str, Any], filters: dict[str, Any]) -> Any:
        return self.db.update(self.table_name, data, filters)

    def delete(self, filters: dict[str, Any]) -> Any:
        return self.db.delete(self.table_name, filters)