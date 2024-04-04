from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column, relationship
from sqlalchemy import ForeignKey
from typing import List

class Base(DeclarativeBase):
    pass

class Skin(Base):
    __tablename__ = "skins"
    id:Mapped[int] = mapped_column(primary_key=True)
    name:Mapped[str] = mapped_column(nullable=False)
    market_hash_name:Mapped[str] = mapped_column(nullable=False)
    sell_price_text:Mapped[float] = mapped_column(nullable=False)
    icon_url:Mapped[str] = mapped_column(nullable=False)

    def __repr__(self):
        return f"Name = {self.name}\nPrice = {self.sell_price_text}\nName = https://community.cloudflare.steamstatic.com/economy/image/{self.icon_url}\n"