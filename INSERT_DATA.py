import yfinance as yf
from sqlalchemy import create_engine
import pandas as pd
from datetime import datetime

engine = create_engine("sqlite:///database.db")

tick = "AAPL"
df = yf.Ticker(tick).history("10y", interval="1d")

# df.reset_index(inplace=True)
# df.rename(columns={"Date":"Datetime"}, inplace=True)
df.index.names = ["Datetime"]
df.drop(["Stock Splits", "Dividends"], axis=1, inplace=True)

df["Ticker"] = tick
df["InsertTime"] = datetime.now()

df.to_sql("Ticker_1D", con=engine, if_exists="append")
print(df.head())