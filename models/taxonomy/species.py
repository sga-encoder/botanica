from pydantic import BaseModel, validator, ValidationError

class Species(BaseModel):
    id: str
    scientific_name: str
    id_genus: str

    @validator('id')
    def id_validator(cls, value):
        if not value or len(value) == 0:
            raise ValueError('El id no puede estar vacío')
        return value

    @validator('scientific_name')
    def scientific_name_validator(cls, value):
        if not value or len(value) == 0:
            raise ValueError('El scientific_name no puede estar vacío')
        if len(value) > 150:
            raise ValueError('El scientific_name no puede tener más de 150 caracteres')
        return value

    @validator('id_genus')
    def id_genus_validator(cls, value):
        if not value or len(value) == 0:
            raise ValueError('El id_genus no puede estar vacío')
        return value