from pydantic import BaseModel, validator, ValidationError

class Usages(BaseModel):
    id: str
    description_usage: str

    @validator('id')
    def id_validator(cls, value):
        if not value or len(value) == 0:
            raise ValueError('El id no puede estar vacío')
        return value

    @validator('description_usage')
    def description_usage_validator(cls, value):
        if not value or len(value) == 0:
            raise ValueError('La descripción del uso no puede estar vacía')
        return value
