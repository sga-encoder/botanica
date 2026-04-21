from pydantic import BaseModel, validator, ValidationError

class Image(BaseModel):
    id: str
    id_species: str
    file_path: str
    description: str

    @validator('id')
    def id_validator(cls, value):
        if not value or len(value) == 0:
            raise ValueError('El id no puede estar vacío')
        return value

    @validator('id_species')
    def id_species_validator(cls, value):
        if not value or len(value) == 0:
            raise ValueError('El id_species no puede estar vacío')
        return value

    @validator('file_path')
    def file_path_validator(cls, value):
        if not value or len(value) == 0:
            raise ValueError('El file_path no puede estar vacío')
        if len(value) > 255:
                raise ValueError('El file_path no puede tener más de 255 caracteres')
        return value
    
    @validator('description')
    def description_validator(cls, value):
        if not value or len(value) == 0:
            raise ValueError('La description no puede estar vacía')
        return value