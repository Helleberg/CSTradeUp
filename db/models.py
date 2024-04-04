from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column, relationship
from sqlalchemy import ForeignKey
from typing import List

class Base(DeclarativeBase):
    pass

class Skin(Base):
    __tablename__ = "skins"
    id:Mapped[int] = mapped_column(primary_key=True)
    name:Mapped[str] = mapped_column(nullable=False)
    price:Mapped[float] = mapped_column(nullable=False)
    collection_id:Mapped[int] = mapped_column(nullable=False)
    quality_id:Mapped[int] = mapped_column(nullable=False)
    min_float:Mapped[float] = mapped_column(nullable=False)
    max_float:Mapped[float] = mapped_column(nullable=False)

    def __repr__(self):
        return f"Name = {self.name}\nPrice = {self.price}\n"