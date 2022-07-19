from typing import List, Optional

from sqlmodel import Field, Relationship, SQLModel


class List(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    name: str

    tasks: List["task"] = Relationship(back_populates="list")


