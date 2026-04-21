from pydantic import BaseModel, validator, ValidationError

class EmbeddingImage(BaseModel):
    id: str
    id_image: str
    vector_embedding: list[float]

    @validator('id')
    def id_validator(cls, value):
        if not value or len(value) == 0:
            raise ValueError('El id no puede estar vacío')
        return value

    @validator('id_image')
    def id_image_validator(cls, value):
        if not value or len(value) == 0:
            raise ValueError('El id_image no puede estar vacío')
        return value

    @validator('vector_embedding')
    def vector_embedding_validator(cls, value):
        if not value or len(value) == 0:
            raise ValueError('El vector_embedding no puede estar vacío')
        return value