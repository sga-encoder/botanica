from pydantic import BaseModel, validator, ValidationError

class Family(BaseModel):
    id: str
    name: str

    @validator('id')
    def id_validator(cls, value):
        if not value or len(value) == 0:
            raise ValueError('El id no puede estar vacío')
        return value

    @validator('name')
    def name_validator(cls, value):
        if not value or len(value) == 0:
            raise ValueError('El name no puede estar vacío')
        if len(value) > 100:
            raise ValueError('El name no puede tener más de 100 caracteres')
        return value