from sqlalchemy import create_engine
import pandas as pd
from datetime import datetime

engine = create_engine("sqlite:///database.db")

# df = pd.read_csv("./CSVs/InterestRates.csv")
# metric = "IRATE"

# df = pd.read_csv("./CSVs/ConsumerSentimentIndex.csv")
# metric = "CSI"

df = pd.read_csv("./CSVs/UnemploymentRates.csv")
metric = "URATE"


df.columns = ["Datetime", "Rate"]

df["Datetime"] = pd.to_datetime(df["Datetime"])
df["Rate"] = pd.to_numeric(df["Rate"])
df["Metric"] = metric
df["InsertTime"] = datetime.now()

df.to_sql("Macroeconomic_Data", con=engine, if_exists="append", index=False)
print(df.head())