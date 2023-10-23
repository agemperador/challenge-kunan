from sqlalchemy import Integer, String
from sqlalchemy.orm import Mapped, mapped_column

from app.adapters.database import database


class ElementDB(database.db.Model):
    """
        Entidad asociada al orm
    """
    __tablename__ = 'ElementsToProcess'
    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    idBulk: Mapped[int] = mapped_column(Integer, nullable=False)
    status: Mapped[int] = mapped_column(Integer, nullable=False)
    retries: Mapped[int] = mapped_column(Integer,nullable=False)
    name: Mapped[str] = mapped_column(String, nullable=False, unique=True)