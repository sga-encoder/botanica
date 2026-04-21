from pydantic import BaseModel, validator, ValidationError

class AltitudinalRange(BaseModel):
    id: str
    min_altitude: int
    max_altitude: int
    id_species: str

    @validator('id')
    def id_validator(cls, value):
        if not value or len(value) == 0:
            raise ValueError('El id no puede estar vacío')
        return value
    @validator('min_altitude')
    def min_altitude_validator(cls, value):
        if value < 0:
            raise ValueError('La altitud mínima no puede ser negativa')
        return value

    @validator('max_altitude')
    def max_altitude_validator(cls, value):
        if value < 0:
            raise ValueError('La altitud máxima no puede ser negativa')
        return value
    
    @validator('id_species')
    def id_species_validator(cls, value):
        if not value or len(value) == 0:
            raise ValueError('El id_species no puede estar vacío')
        return value