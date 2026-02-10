
import sqlite3

conn = sqlite3.connect("database.db")
cur = conn.cursor()


tick = "CSCO"
cur.execute("""    
DELETE FROM Ticker_1H
WHERE Ticker = 'TSLA'
""")

conn.commit()
conn.close()