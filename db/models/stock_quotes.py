from sqlalchemy import Column, Integer, String, Boolean, Date, ForeignKey, Float
from sqlalchemy.orm import relationship

from db.base_class import Base


class StockQuotes(Base):
    id = Column(Integer, primary_key=True, index=True)
    date = Column(Date, nullable=False)
    open_price = Column(Float, nullable=False)
    high_price = Column(Float, nullable=False)
    low_price = Column(Float, nullable=False)
    close_price = Column(Float, nullable=False)
    volume = Column(Integer, nullable=False)
    stock_symbol = Column(String, ForeignKey("stocks.company_symbol"), nullable=False)

    stocks = relationship("Stocks", back_populates='stock_quotes')
