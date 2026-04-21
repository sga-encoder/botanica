from pydantic import BaseModel, validator, ValidationError

class EmbeddingText(BaseModel):
    id: str
    id_chunk: str
    vector_embedding: list[float]
    model_version: str

    @validator('id')
    def id_validator(cls, value):
        if not value or len(value) == 0:
            raise ValueError('El id no puede estar vacío')
        return value

    @validator('id_chunk')
    def id_chunk_validator(cls, value):
        if not value or len(value) == 0:
            raise ValueError('El id_chunk no puede estar vacío')
        return value

    @validator('vector_embedding')
    def vector_embedding_validator(cls, value):
        if not value or len(value) == 0:
            raise ValueError('El vector_embedding no puede estar vacío')
        return value

    @validator('model_version')
    def model_version_validator(cls, value):
        if not value or len(value) == 0:
            raise ValueError('La model_version no puede estar vacía')
        if len(value) > 150:
            raise ValueError('La model_version no puede tener más de 150 caracteres')
        return value