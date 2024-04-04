from sqlalchemy import create_engine

# echo=True for debug
engine = create_engine("sqlite:///db/CSTradeUp.db", echo=True)