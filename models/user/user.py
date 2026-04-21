from pydantic import BaseModel, validator, ValidationError

class User(BaseModel):
    id: str
    name: str
    email: str
    id_role: str

    @validator('id')
    def id_validator(cls, value):
        if not value or len(value) == 0:
            raise ValueError('El id no puede estar vacío')
        return value

    @validator('name')
    def name_validator(cls, value):
        if not value or len(value) == 0:
            raise ValueError('El nombre no puede estar vacío')
        if len(value) > 100:
            raise ValueError('El nombre no puede tener más de 100 caracteres')
        return value

    @validator('email')
    def email_validator(cls, value):
        if not value or len(value) == 0:
            raise ValueError('El email no puede estar vacío')
        if len(value) > 100:
            raise ValueError('El email no puede tener más de 100 caracteres')
        if '@' not in value:
            raise ValueError('El email debe contener @')
        return value

    @validator('id_role')
    def id_role_validator(cls, value):
        if not value or len(value) == 0:
            raise ValueError('El id_role no puede estar vacío')
        return value


