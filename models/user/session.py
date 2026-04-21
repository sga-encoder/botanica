from pydantic import BaseModel, validator, ValidationError
from datetime import datetime

class Session(BaseModel):
    id: str
    id_user: str
    start_date: datetime

    @validator('id')
    def id_validator(cls, value):
        if not value or len(value) == 0:
            raise ValueError('El id no puede estar vacío')
        return value

    @validator('id_user')
    def id_user_validator(cls, value):
        if not value or len(value) == 0:
            raise ValueError('El id_user no puede estar vacío')
        return value

    @validator('start_date')
    def start_date_validator(cls, value):
        if not value:
            raise ValueError('La fecha de inicio no puede estar vacía')
        return value