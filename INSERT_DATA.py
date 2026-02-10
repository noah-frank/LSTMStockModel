import yfinance as yf
from sqlalchemy import create_engine
import pandas as pd
from datetime import datetime

engine = create_engine("sqlite:///database.db")

tick = "XPO"
df = yf.Ticker(tick).history("2y", interval="1h")

# df.reset_index(inplace=True)
# df.rename(columns={"Date":"Datetime"}, inplace=True)
df.index.names = ["Datetime"]
df.drop(["Stock Splits", "Dividends"], axis=1, inplace=True)

df["Ticker"] = tick
df["InsertTime"] = datetime.now()

df.to_sql("Ticker_1H", con=engine, if_exists="append")
print(df.head())