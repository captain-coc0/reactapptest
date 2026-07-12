import sqlite3
from pathlib import Path
import json

DB_PATH = Path(__file__).with_name("apptest.db")

def get_db():
    """
    Creates a connection to the database on call. 
    Commands can be executed
    """
    #connect to the db file
    conn = sqlite3.connect(DB_PATH)
    #this turns the rows in the database into a readable python dict
    conn.row_factory = sqlite3.Row
    return conn

def init_db():
    with get_db() as conn:
        #create a table containing text strings
        conn.execute("""
           CREATE TABLE IF NOT EXISTS texts (
               id INTEGER PRIMARY KEY AUTOINCREMENT,
               name TEXT NOT NULL,
               content TEXT NOT NULL,
               created_at TEXT NOT NULL DEFAULT CURRENT_TIMESTAMP
           )         
        """)

def load_text(id):
    with get_db() as conn:
        print(id)
        #obtain a text
        row = conn.execute("""
            SELECT content FROM texts WHERE id = ?                   
        """, (id,)).fetchone()
    if row:
        #json.loads turns row into a python dictionary
        return dict(row)["content"]
    
    return None