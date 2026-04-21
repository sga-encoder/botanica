from pydantic import BaseModel, validator, ValidationError
from datetime import datetime

class Query(BaseModel):
    id: str
    id_session: str
    query_text: str
    date: datetime

    @validator('id')
    def id_validator(cls, value):
        if not value or len(value) == 0:
            raise ValueError('El id no puede estar vacío')
        return value

    @validator('id_session')
    def id_session_validator(cls, value):
        if not value or len(value) == 0:
            raise ValueError('El id_session no puede estar vacío')
        return value

    @validator('query_text')
    def query_text_validator(cls, value):
        if not value or len(value) == 0:
            raise ValueError('El query_text no puede estar vacío')
        return value
    
    @validator('date')
    def date_validator(cls, value):
        if not value:
            raise ValueError('La fecha no puede estar vacía')
        return value