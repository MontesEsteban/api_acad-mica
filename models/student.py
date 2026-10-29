from sqlmodel import SQLModel, Field


class Student(SQLModel, table=True):
    id: int | None = Field(default=None, primary_key=True)
    name: str = Field(min_length=3, max_length=80)
    email: str
    semester: int = Field(ge=1, le=10)
    active: bool = True
