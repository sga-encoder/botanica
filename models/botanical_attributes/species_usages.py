from pydantic import BaseModel, validator, ValidationError

class SpeciesUsages(BaseModel):
    id_species: str
    id_usage: str

    @validator('id_species')
    def id_species_validator(cls, value):
        if not value or len(value) == 0:
            raise ValueError('El id_species no puede estar vacío')
        return value

    @validator('id_usage')
    def id_usage_validator(cls, value):
        if not value or len(value) == 0:
            raise ValueError('El id_usage no puede estar vacío')
        return value