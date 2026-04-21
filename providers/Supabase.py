import os
from functools import lru_cache
from typing import Any

from dotenv import load_dotenv
from supabase import Client, create_client

load_dotenv()


def _required_env(name: str) -> str:
    value = os.getenv(name)
    if not value:
        raise RuntimeError(f'Falta definir la variable de entorno {name}')
    return value


@lru_cache(maxsize=1)
def get_supabase_client() -> Client:
    return create_client(_required_env("SUPABASE_URL"), _required_env("SUPABASE_KEY"))


class Supabase:
    def __init__(self, client: Client | None = None):
        self.client = client or get_supabase_client()

    def find_many(self, table: str, filters: dict[str, Any] | None = None, limit: int | None = None):
        query = self.client.table(table).select("*")
        query = self._apply_filters(query, filters)
        if limit is not None:
            query = query.limit(limit)
        response = query.execute()
        return response.data or []

    def find_one(self, table: str, filters: dict[str, Any] | None = None):
        records = self.find_many(table, filters=filters, limit=1)
        return records[0] if records else None

    def create(self, table: str, data: dict[str, Any] | list[dict[str, Any]]):
        response = self.client.table(table).insert(data).execute()
        return response.data

    def update(self, table: str, data: dict[str, Any], filters: dict[str, Any]):
        query = self.client.table(table).update(data)
        query = self._apply_filters(query, filters)
        response = query.execute()
        return response.data

    def delete(self, table: str, filters: dict[str, Any]):
        query = self.client.table(table).delete()
        query = self._apply_filters(query, filters)
        response = query.execute()
        return response.data

    def _apply_filters(self, query, filters: dict[str, Any] | None = None):
        if not filters:
            return query
        for key, value in filters.items():
            query = query.eq(key, value)
        return query
