"""
> Defines Pydantic models(schemas) for request validation and response formatting
> Promotes data consistency and validation against invalid inputs

orm_mode = True:
 > Allows Pydantic to read data directly from ORM objects (SQLAlchemy models)
 > Enables smooth conversion to JSON.
"""

from pydantic import BaseModel, EmailStr
# from typing import Optional


class EmployeeBase(BaseModel):
    name: str
    email: EmailStr


class EmployeeCreate(EmployeeBase):
    # email: Optional[EmailStr]
    pass


class EmployeeUpdate(EmployeeBase):
    pass


class EmployeeOut(EmployeeBase):
    id: int

    class Config:
        orm_mode = True

