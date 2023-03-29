import sqlite3
from datetime import datetime

def store_net_balance(date, net_balance):
    # Connect to the SQLite database (this will create a new file named 'ynab.db' if it doesn't exist)
    conn = sqlite3.connect("ynab.db")
    cursor = conn.cursor()

    # Create the 'net_balance' table if it doesn't exist
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS net_balance (
        id INTEGER PRIMARY KEY,
        date DATE UNIQUE,
        balance INTEGER
    )
    """)

    # Insert or update the net balance for the given date
    cursor.execute("""
    INSERT OR REPLACE INTO net_balance (date, balance)
    VALUES (?, ?)
    """, (date, net_balance))

    # Commit the changes and close the connection
    conn.commit()
    conn.close()

def fetch_net_balance_data(days=30):
    # Connect to the SQLite database
    conn = sqlite3.connect("ynab.db")
    cursor = conn.cursor()

    # Fetch the net balance data for the past days
    end_date = datetime.date.today()
    start_date = end_date - datetime.timedelta(days=days - 1)
    cursor.execute("""
    SELECT date, balance
    FROM net_balance
    WHERE date BETWEEN ? AND ?
    ORDER BY date
    """, (start_date, end_date))

    data = cursor.fetchall()

    # Close the connection
    conn.close()

    return data
