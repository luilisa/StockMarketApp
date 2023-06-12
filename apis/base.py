from fastapi import APIRouter

from apis.version1 import route_general_pages, route_users, route_companies, route_news, route_stocks, route_stock_quotes, route_portfolios

api_router = APIRouter()
api_router.include_router(route_general_pages.general_pages_router,prefix="",tags=["general_pages"])
api_router.include_router(route_users.router, prefix="/users", tags=["users"])
api_router.include_router(route_companies.router, prefix="/companies", tags=["companies"])
api_router.include_router(route_news.router, prefix="/news", tags=["news"])
api_router.include_router(route_stocks.router, prefix="/stocks", tags=["stocks"])
api_router.include_router(route_stock_quotes.router, prefix="/stock_quotes", tags=["stock_quotes"])
api_router.include_router(route_portfolios.router, prefix="/portfolios", tags=["portfolios"])