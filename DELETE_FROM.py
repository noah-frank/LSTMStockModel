
import sqlite3

conn = sqlite3.connect("database.db")
cur = conn.cursor()


tick = "AAPL"
cur.execute("""    
DELETE FROM Ticker_1D WHERE Ticker = 'AAPL'
""")

conn.commit()
conn.close()