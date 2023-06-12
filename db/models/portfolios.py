from sqlalchemy import Column, Integer, String, Boolean, Date, ForeignKey
from sqlalchemy.orm import relationship

from db.base_class import Base


class Portfolios(Base):
    id = Column(Integer, primary_key=True, index=True)
    portfolio_name = Column(String, nullable=False)
    owner_email = Column(String, ForeignKey("users.email"), nullable=False)

    users = relationship("Users", back_populates='portfolios')
    # stocks = relationship("StocksInPortfolio",  back_populates="portfolios")
    stocks = relationship("Stocks", secondary="stocksinportfolio", back_populates="portfolios")