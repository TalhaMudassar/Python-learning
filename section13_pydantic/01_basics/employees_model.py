from typing import Optional
from pydantic import BaseModel, Field

class Employee(BaseModel):
    id: int
    name: str = Field(
        ...,
        min_length=3,
        max_length=50,
        description="Employee Name",
        examples=["Hiesh Choudhary"]
    )
    department: Optional[str] = "General"
    salary: float = Field(
        ...,
        ge=1000,
        le=1_000_000,
        description="Annual salary in USD"
    )


class User(BaseModel):
    email: str = Field(
        ...,
        pattern=r'^[\w\.-]+@[\w\.-]+\.\w+$',
        description="Valid email address"
    )
    phone: str = Field(
        ...,
        pattern=r'^\+?\d{10,15}$',
        description="Phone number with optional + and 10–15 digits"
    )
    age: int = Field(
        ...,
        ge=0,
        le=150,
        description="Age in years"
    )
    discount: float = Field(
        ...,
        ge=0,
        le=1000,
        description="Discount percentage"
    )
