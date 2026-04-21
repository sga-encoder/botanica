from __future__ import annotations

from abc import ABC, abstractmethod
from typing import Any, Generic, TypeVar

T = TypeVar("T")


class ServiceInterface(ABC, Generic[T]):
    @abstractmethod
    def get_by_id(self, record_id: int | str) -> T | None:
        raise NotImplementedError

    @abstractmethod
    def get_one(self, filters: dict[str, Any]) -> T | None:
        raise NotImplementedError

    @abstractmethod
    def get_many(self, filters: dict[str, Any] | None = None, limit: int | None = None) -> list[T]:
        raise NotImplementedError

    @abstractmethod
    def create(self, data: dict[str, Any] | list[dict[str, Any]]) -> Any:
        raise NotImplementedError

    @abstractmethod
    def update(self, data: dict[str, Any], filters: dict[str, Any]) -> Any:
        raise NotImplementedError

    @abstractmethod
    def delete(self, filters: dict[str, Any]) -> Any:
        raise NotImplementedError