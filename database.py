import sqlite3
from datetime import datetime


def init_db():
    conn = sqlite3.connect('calls.db')
    c = conn.cursor()
    c.execute('''
        CREATE TABLE IF NOT EXISTS calls(
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            call_id TEXT UNIQUE,
            phone_number TEXT,
            timestamp TEXT,
            duration INTEGER,
            transcript TEXT,
            summary TEXT,
            cost REAL
        )
    ''')
    conn.commit()
    conn.close()

def save_call(call_data):
    conn=sqlite3.connect('calls.db')
    c=conn.cursor()

    c.execute('''
        INSERT OR REPLACE INTO calls
        (call_id,phone_number, timestamp, duration,transcript, summary, cost)
        VALUES( ?,?,?,?,?,?,?)
    ''',(
        call_data.get('call_id'),
        call_data.get('phone_number'),
        datetime.now().isoformat(),
        call_data.get('duration'),
        call_data.get('transcript'),
        call_data.get('summary'),
        call_data.get('cost')
    ))
    conn.commit()
    conn.close()

def get_all_calls():
    conn=sqlite3.connect('calls.db')
    conn.row_factory = sqlite3.Row
    c= conn.cursor()
    c.execute('SELECT * FROM calls ORDER BY timestamp DESC')
    calls =c.fetchall()
    conn.close()
    return calls


