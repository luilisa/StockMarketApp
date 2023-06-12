from sqlalchemy import Column, Integer, String, Boolean, Date, ForeignKey, Float
from sqlalchemy.orm import relationship

from db.base_class import Base


class StocksInPortfolio(Base):
    portfolio_id = Column(Integer, ForeignKey("portfolios.id"), nullable=1, primary_key=True)
    stock_id = Column(Integer, ForeignKey("stocks.id"), nullable=False, primary_key=True)

    # stocks = relationship("Stocks", back_populates="portfolios")
    # portfolios = relationship("Portfolios", back_populates="stocks")