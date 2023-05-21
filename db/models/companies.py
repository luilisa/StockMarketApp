from sqlalchemy import Column, Integer, String, Boolean, Date, ForeignKey
from sqlalchemy.orm import relationship

from db.base_class import Base


class Companies(Base):
    id = Column(Integer, primary_key=True, index=True)
    company_name = Column(String, unique=True, nullable=False)
    symbol = Column(String, nullable=False, unique=True, index=True)
    sector = Column(String)
    news = relationship("News", back_populates="companies")
    # stocks = relationship("Stocks", back_populates="companies")
