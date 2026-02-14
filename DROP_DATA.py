import sqlite3

conn = sqlite3.connect("database.db")
cur = conn.cursor()

tick = "AAPL"
cur.execute(
"""

DELETE FROM Ticker_1D
WHERE Ticker = "AAPL" AND Ticker + CAST(InsertTime AS varchar) NOT IN 
(
    SELECT Ticker + CAST(MAX(InsertTime) AS varchar) AS 'MaxInsert' 
    FROM Ticker_1D
    WHERE Ticker = "AAPL"
    GROUP BY Ticker
)
""")

conn.commit()
conn.close()