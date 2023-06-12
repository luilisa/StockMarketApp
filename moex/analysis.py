from datetime import datetime, timedelta
from sqlalchemy import create_engine, Column, Integer, Float, String, DateTime
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.sql import func

import pandas as pd
from db.models.stock_quotes import StockQuotes
import matplotlib.pyplot as plt
from db.models.stocks import Stocks
from session import DatabaseSession


# # Создание модели данных акции
# Base = declarative_base()
#
# class StockPrice(Base):
#     __tablename__ = 'stock_prices'
#
#     id = Column(Integer, primary_key=True)
#     symbol = Column(String)
#     date = Column(DateTime)
#     price = Column(Float)

# # Установка соединения с базой данных
# engine = create_engine('your_database_connection_string')
# Session = sessionmaker(bind=engine)
# session = Session()

# Получение последних 50 дней
end_date = datetime.now().date()
start_date = end_date - timedelta(days=29)

# Запрос к базе данных для получения цен акции за последние 50 дней
def get_prices(ticker):
    with DatabaseSession() as session:
        query = session.query(StockQuotes).filter(
            StockQuotes.stock_symbol == ticker,
        ).order_by(StockQuotes.date)

        df = pd.read_sql(query.statement, session.bind)

        # Преобразование столбца 'date' в тип datetime
        df['date'] = pd.to_datetime(df['date'])
        prices = [row.close_price for row in query.all()]

        print('prices', prices)

        window_size = 5
        df['moving_average'] = df['close_price'].rolling(window=window_size).mean()

        # Вывод значений скользящего среднего
        moving_averages = df['moving_average'].tolist()
        print('mov av', moving_averages)

        # Создание DataFrame для удобства работы с данными
        df = pd.DataFrame({'Moving Average': moving_averages})

        # Создание графика
        plt.plot(df.index, df['Moving Average'], label='Moving Average')

        # Добавление заголовка и меток осей
        plt.title('Moving Average')
        plt.xlabel('Time')
        plt.ylabel('Value')

        # Отображение легенды
        plt.legend()

        # Отображение графика
        plt.show()

# Вычисление скользящего среднего

print(get_prices('AFLT'))
# Вывод значений скользящего среднего

