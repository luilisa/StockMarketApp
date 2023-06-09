from sqlalchemy import Column, Integer, String, Boolean, Date, ForeignKey, Float
from sqlalchemy.orm import relationship

from db.base_class import Base


class Stocks(Base):
    id = Column(Integer, primary_key=True, index=True)
    # company_symbol = Column(String, ForeignKey("companies.symbol"), nullable=False)
    # company_symbol = Column(String, nullable=False)
    company_name = Column(String, nullable=False)
    company_symbol = Column(String, nullable=False, unique=True)
    stock_price = Column(Float, nullable=False)

    # companies = relationship("Companies", back_populates='stocks')
    stock_quotes = relationship("StockQuotes", back_populates='stocks')
    portfolios = relationship("Portfolios",  secondary="stocksinportfolio", back_populates="stocks")
