from __future__ import annotations

import unittest
from datetime import datetime
from types import GenericAlias
from typing import Any, get_args, get_origin, cast

import models
from domain import services, repositories


class FakeDBAdapter:
    def __init__(self, one_row: dict[str, Any], many_rows: list[dict[str, Any]] | None = None):
        self.one_row = one_row
        self.many_rows = many_rows if many_rows is not None else [one_row]
        self.calls: list[tuple[Any, ...]] = []

    def find_one(self, table: str, filters: dict[str, Any] | None = None):
        self.calls.append(("find_one", table, filters))
        return self.one_row

    def find_many(self, table: str, filters: dict[str, Any] | None = None, limit: int | None = None):
        self.calls.append(("find_many", table, filters, limit))
        data = self.many_rows
        return data if limit is None else data[:limit]

    def create(self, table: str, data: dict[str, Any] | list[dict[str, Any]]):
        self.calls.append(("create", table, data))
        return data

    def update(self, table: str, data: dict[str, Any], filters: dict[str, Any]):
        self.calls.append(("update", table, data, filters))
        return [data]

    def delete(self, table: str, filters: dict[str, Any]):
        self.calls.append(("delete", table, filters))
        return [{"deleted": True}]


class FakeRepository:
    def __init__(self, model_instance: Any):
        self.model_instance = model_instance
        self.calls: list[tuple[Any, ...]] = []

    def find_by_id(self, record_id: int | str):
        self.calls.append(("find_by_id", record_id))
        return self.model_instance

    def find_one(self, filters: dict[str, Any]):
        self.calls.append(("find_one", filters))
        return self.model_instance

    def find_many(self, filters: dict[str, Any] | None = None, limit: int | None = None):
        self.calls.append(("find_many", filters, limit))
        return [self.model_instance]

    def create(self, data: dict[str, Any] | list[dict[str, Any]]):
        self.calls.append(("create", data))
        return data

    def update(self, data: dict[str, Any], filters: dict[str, Any]):
        self.calls.append(("update", data, filters))
        return [data]

    def delete(self, filters: dict[str, Any]):
        self.calls.append(("delete", filters))
        return [{"deleted": True}]


def _model_fields(model_cls: type[Any]) -> dict[str, Any]:
    if hasattr(model_cls, "model_fields"):
        return model_cls.model_fields
    if hasattr(model_cls, "__fields__"):
        return model_cls.__fields__
    return {}


def _annotation_from_field(field: Any) -> Any:
    if hasattr(field, "annotation"):
        return field.annotation
    if hasattr(field, "type_"):
        return field.type_
    return str


def _value_for(field_name: str, annotation: Any) -> Any:
    origin = get_origin(annotation)
    args = get_args(annotation)

    if field_name == "email":
        return "test@example.com"
    if field_name in {"faithfulness", "answer_relevance", "context_recall"}:
        return 0.8

    if origin is list and args and args[0] is float:
        return [0.1, 0.2, 0.3]

    if origin is not None and args:
        non_none = [a for a in args if a is not type(None)]
        if non_none:
            return _value_for(field_name, non_none[0])

    if annotation is str:
        return f"{field_name}_value"
    if annotation is int:
        return 1
    if annotation is float:
        return 0.5
    if annotation is datetime:
        return datetime(2026, 4, 20, 10, 0, 0)

    return f"{field_name}_value"


def _build_row_for_model(model_cls: type[Any]) -> dict[str, Any]:
    row: dict[str, Any] = {}
    for name, field in _model_fields(model_cls).items():
        row[name] = _value_for(name, _annotation_from_field(field))
    return row


def _model_from_repository_cls(repository_cls: type[Any]) -> type[Any]:
    annotation = repository_cls._to_model.__annotations__.get("return")
    if isinstance(annotation, str):
        return getattr(models, annotation)
    return annotation


def _model_from_service_cls(service_cls: type[Any]) -> type[Any]:
    for base in getattr(service_cls, "__orig_bases__", []):
        origin = get_origin(base)
        if origin is not None:
            args = get_args(base)
            if args:
                return args[0]
        if isinstance(base, GenericAlias) and base.__args__:
            return base.__args__[0]
    raise AssertionError(f"No se pudo inferir el modelo de {service_cls.__name__}")


def _safe_name(name: str) -> str:
    return name.lower().replace(" ", "_")


class AllRepositoriesAndServicesTests(unittest.TestCase):
    pass


def _make_repository_test(repository_name: str):
    def test(self):
        repository_cls = getattr(repositories, repository_name)
        model_cls = _model_from_repository_cls(repository_cls)
        row = _build_row_for_model(model_cls)
        fake_db = FakeDBAdapter(one_row=row, many_rows=[row, row])

        repo = repository_cls(fake_db)

        one = repo.find_by_id("1")
        many = repo.find_many(limit=2)
        created = repo.create({"name": "x"})
        updated = repo.update({"name": "y"}, {"id": "1"})
        deleted = repo.delete({"id": "1"})

        self.assertIsInstance(one, model_cls, msg=f"{repository_name}: find_by_id debe devolver {model_cls.__name__}")
        self.assertEqual(len(many), 2, msg=f"{repository_name}: find_many debe devolver 2 registros")
        self.assertIsInstance(many[0], model_cls, msg=f"{repository_name}: find_many debe mapear cada fila a {model_cls.__name__}")
        self.assertEqual(created, {"name": "x"}, msg=f"{repository_name}: create debe delegar el payload")
        self.assertEqual(updated, [{"name": "y"}], msg=f"{repository_name}: update debe delegar el payload")
        self.assertEqual(deleted, [{"deleted": True}], msg=f"{repository_name}: delete debe delegar el filtro")

    return test


def _make_service_test(service_name: str):
    def test(self):
        service_cls = getattr(services, service_name)
        model_cls = _model_from_service_cls(service_cls)
        row = _build_row_for_model(model_cls)
        model_instance = model_cls(**row)
        fake_repo = FakeRepository(model_instance)

        service = service_cls.__new__(service_cls)
        service.repo = fake_repo

        one = service.get_by_id("1")
        first = service.get_one({"id": "1"})
        many = service.get_many(limit=1)
        created = service.create({"name": "x"})
        updated = service.update({"name": "y"}, {"id": "1"})
        deleted = service.delete({"id": "1"})

        self.assertIsInstance(one, model_cls, msg=f"{service_name}: get_by_id debe devolver {model_cls.__name__}")
        self.assertIsInstance(first, model_cls, msg=f"{service_name}: get_one debe devolver {model_cls.__name__}")
        self.assertEqual(len(many), 1, msg=f"{service_name}: get_many debe devolver 1 registro")
        self.assertEqual(created, {"name": "x"}, msg=f"{service_name}: create debe delegar el payload")
        self.assertEqual(updated, [{"name": "y"}], msg=f"{service_name}: update debe delegar el payload")
        self.assertEqual(deleted, [{"deleted": True}], msg=f"{service_name}: delete debe delegar el filtro")

    return test


for repository_name in repositories.__all__:
    if repository_name in {"BaseRepository"}:
        continue
    test_name = f"test_repository_{_safe_name(repository_name)}_main_methods"
    setattr(AllRepositoriesAndServicesTests, test_name, _make_repository_test(repository_name))


for service_name in services.__all__:
    if service_name in {"ServiceInterface", "RepositoryService", "BaseRepositoryService"}:
        continue
    test_name = f"test_service_{_safe_name(service_name)}_main_methods"
    setattr(AllRepositoriesAndServicesTests, test_name, _make_service_test(service_name))


def _test_user_service_get_user_info(self):
    row = _build_row_for_model(models.User)
    model_instance = models.User(**row)

    service = services.UserService.__new__(services.UserService)
    service.repo = cast(Any,FakeRepository(model_instance))

    user_info = service.get_user_info(123)

    assert user_info is not None
    
    self.assertIsInstance(user_info, dict, msg="UserService: get_user_info debe devolver un diccionario")
    self.assertEqual(user_info["email"], row["email"], msg="UserService: get_user_info debe preservar el email del usuario")


setattr(AllRepositoriesAndServicesTests, "test_user_service_get_user_info", _test_user_service_get_user_info)


if __name__ == "__main__":
    unittest.main(verbosity=2)