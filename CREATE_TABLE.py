import sqlite3

conn = sqlite3.connect("database.db")
cur = conn.cursor()

# cur.execute("DROP TABLE Ticker_1H;")
# conn.commit()

cur.execute("""    
CREATE TABLE Ticker_1D (
            ID integer primary key,
            Datetime datetime,
            Open real,
            High real,
            Low real,
            Close real,
            Volume real,
            Ticker text,
            InsertTime datetime
            )
""")

conn.commit()
conn.close()