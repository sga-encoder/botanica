from pydantic import BaseModel, validator, ValidationError

class Evaluation(BaseModel):
    id: str
    id_query: str
    faithfulness: float
    answer_relevance: float
    context_recall: float

    @validator('id')
    def id_validator(cls, value):
        if not value or len(value) == 0:
            raise ValueError('El id no puede estar vacío')
        return value

    @validator('id_query')
    def id_query_validator(cls, value):
        if not value or len(value) == 0:
            raise ValueError('El id_query no puede estar vacío')
        return value

    @validator('faithfulness')
    def faithfulness_validator(cls, value):
        if value is None:
            raise ValueError('El faithfulness no puede estar vacío')
        if not (0 <= value <= 1):
            raise ValueError('El faithfulness debe estar entre 0 y 1')
        return value

    @validator('answer_relevance')
    def answer_relevance_validator(cls, value):
        if value is None:
            raise ValueError('El answer_relevance no puede estar vacío')
        if not (0 <= value <= 1):
            raise ValueError('El answer_relevance debe estar entre 0 y 1')
        return value
    
    @validator('context_recall')
    def context_recall_validator(cls, value):
        if value is None:
            raise ValueError('El context_recall no puede estar vacío')
        if not (0 <= value <= 1):
            raise ValueError('El context_recall debe estar entre 0 y 1')
        return value