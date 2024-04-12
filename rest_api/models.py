from typing import Optional, List
from uuid import UUID, uuid4
from enum import Enum
from pydantic import BaseModel


class Role(str, Enum):
    admin = 'admin'
    student = 'student'
    user = 'user'
    hokage = 'hokage'


class Gender(str, Enum):
    female = 'female'
    male = 'male'


class User(BaseModel):
    id: Optional[UUID] = uuid4
    first_name: str
    last_name: str
    middle_name: Optional[str] = '-'
    gender: Gender
    roles: List[Role]


