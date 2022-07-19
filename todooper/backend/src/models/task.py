from typing import Optional, List

from sqlmodel import SQLModel, Field, Relationship


class Task(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    text: str
    is_checked: bool

    list_id: Optional[int] = Field(default=None, foreign_key="list.id")
    list: Optional[List] = Relationship(back_populates="tasks")

