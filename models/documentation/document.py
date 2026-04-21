from pydantic import BaseModel, validator, ValidationError

class Document(BaseModel):
    id: str
    id_species: str
    source_url: str
    title: str

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

    @validator('title')
    def title_validator(cls, value):
        if not value or len(value) == 0:
            raise ValueError('El title no puede estar vacío')
        if len(value) > 200:
            raise ValueError('El title no puede tener más de 200 caracteres')
        return value

    @validator('source_url')
    def source_url_validator(cls, value):
        if not value or len(value) == 0:
            raise ValueError('El source_url no puede estar vacío')
        if len(value) > 255:
                raise ValueError('El source_url no puede tener más de 255 caracteres')
        return value