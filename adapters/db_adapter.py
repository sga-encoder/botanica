from typing import Any


class DBAdapter:
    def __init__(self, connection: Any | None = None):
        if connection is None:
            from providers import Supabase

            self.connection = Supabase()
        else:
            self.connection = connection

    def find_many(self, table: str, filters: dict[str, Any] | None = None, limit: int | None = None):
        return self.connection.find_many(table, filters=filters, limit=limit)

    def find_one(self, table: str, filters: dict[str, Any] | None = None):
        return self.connection.find_one(table, filters=filters)

    def create(self, table: str, data: dict[str, Any] | list[dict[str, Any]]):
        return self.connection.create(table, data)

    def update(self, table: str, data: dict[str, Any], filters: dict[str, Any]):
        return self.connection.update(table, data, filters)

    def delete(self, table: str, filters: dict[str, Any]):
        return self.connection.delete(table, filters)
