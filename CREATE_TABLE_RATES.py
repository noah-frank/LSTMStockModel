import sqlite3

conn = sqlite3.connect("database.db")
cur = conn.cursor()

# cur.execute("DROP TABLE Ticker_1H;")
# conn.commit()

cur.execute("""    
CREATE TABLE Macroeconomic_Data (
            ID integer primary key,
            Datetime datetime,
            Rate real,
            Metric text,
            InsertTime datetime
            )
""")

conn.commit()
conn.close()