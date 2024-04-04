from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column, relationship
from sqlalchemy import ForeignKey
from typing import List

class Base(DeclarativeBase):
    pass

class Collection(Base):
    __tablename__ = "collections"
    id:Mapped[int] = mapped_column(primary_key=True)
    name:Mapped[str] = mapped_column(nullable=False)

    def __repr__(self):
        return f"Name = {self.name}\n"
    
class Quality(Base):
    __tablename__ = "qualities"
    id:Mapped[int] = mapped_column(primary_key=True)
    name:Mapped[str] = mapped_column(nullable=False)

    def __repr__(self):
        return f"Name = {self.name}\n"
    
class Condition(Base):
    __tablename__ = "conditions"
    id:Mapped[int] = mapped_column(primary_key=True)
    name:Mapped[str] = mapped_column(nullable=False)

    def __repr__(self):
        return f"Name = {self.name}\n"

class Skin(Base):
    __tablename__ = "skins"
    id:Mapped[int] = mapped_column(primary_key=True)
    name:Mapped[str] = mapped_column(nullable=False)
    price:Mapped[float] = mapped_column(nullable=False)
    min_float:Mapped[float] = mapped_column(nullable=False)
    max_float:Mapped[float] = mapped_column(nullable=False)

    def __repr__(self):
        return f"Name = {self.name}\nPrice = {self.price}\n"
    
### Join tables
class SkinCondition(Base):
    __tablename__ = "skin_condition"
    id:Mapped[int] = mapped_column(primary_key=True)
    skin_id:Mapped[int] = mapped_column(ForeignKey("skins.id"))
    condition_id:Mapped[int] = mapped_column(ForeignKey("conditions.id"))

class SkinCollection(Base):
    __tablename__ = "skin_collection"
    id:Mapped[int] = mapped_column(primary_key=True)
    skin_id:Mapped[int] = mapped_column(ForeignKey("skins.id"))
    condition_id:Mapped[int] = mapped_column(ForeignKey("collections.id"))

class SkinQuality(Base):
    __tablename__ = "skin_quality"
    id:Mapped[int] = mapped_column(primary_key=True)
    skin_id:Mapped[int] = mapped_column(ForeignKey("skins.id"))
    condition_id:Mapped[int] = mapped_column(ForeignKey("qualities.id"))