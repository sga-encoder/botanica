from pydantic import BaseModel, validator, ValidationError

class Chunk(BaseModel):
    id: str
    id_doc: str
    content_text: str
    segment_order: int

    @validator('id')
    def id_validator(cls, value):
        if not value or len(value) == 0:
            raise ValueError('El id no puede estar vacío')
        return value

    @validator('id_doc')
    def id_doc_validator(cls, value):
        if not value or len(value) == 0:
            raise ValueError('El id_doc no puede estar vacío')
        return value

    @validator('content_text')
    def content_text_validator(cls, value):
        if not value or len(value) == 0:
            raise ValueError('El content_text no puede estar vacío')
        return value

    @validator('segment_order')
    def segment_order_validator(cls, value):
        if value is None:
            raise ValueError('El segment_order no puede estar vacío')
        return value