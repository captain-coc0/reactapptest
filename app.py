from flask import Flask, render_template, request
from db import init_db, get_db, load_text
import json
import time

init_db()

#__name__ == name of the module
app = Flask(__name__)


#REST API calls
#we use a decorator here. decorators consist of a 
#function and an inner function, the parent function
#takes a function as an argument, and then the inner
#function will have the decorator logic as well as
#a call to the function we passed into the decorator
#function. this allows us to add extra functionality
#without changing an already existing function. Flask
#is using decorators to basically run our function on
#a specific event such as a get request.
@app.get("/api/health")
def health():
    return{
        "ok" : True,
        "service" : "text-test"
    }

@app.get("/api/debug/testquery")
def testQuery():
    with get_db() as conn:
        res = conn.execute("SELECT * FROM texts").fetchall()
    return {
        "ok" : True,
        "texts" : [dict(row) for row in res]
    }
    
@app.delete("/api/debug/cleartable")
def cleartable():
    with get_db() as conn:
        conn.execute("DELETE FROM texts")
    return {
        "ok" : True,
    }

#when using fetchone(), you recieve the first row in a tuple
#when using fetchall(), you recieve all rows in tuples.
#this should give us texts = [(id, text),...]
@app.get("/api/text/list")
def list_texts():
    with get_db() as conn:
        rows = conn.execute("""
            SELECT id, name FROM texts
            ORDER BY created_at DESC
            """).fetchall()
    return {
        "ok" : True,
        "texts" : [dict(row) for row in rows]
    }

@app.post("/api/text/save")
def saveText():
    #request data on this api call
    data = request.get_json() or {}
    name = data.get("name", "Untitled Text")
    text = data.get("content", "")
    with get_db() as conn:
        conn.execute("""
            INSERT INTO texts (name, content) VALUES (?, ?)
        """, (name, text))
    return {
        "ok" : True,
        "name" : name,
        "content" : text
    }

@app.get("/api/text/<int:textID>/load")
def getTexts(textID):
    res = load_text(textID)
    if res:    
        return {
            "ok" : True,
            "content" : res
        }
    else:
        return {
            "ok" : False
        }

#vite will be serving the UI, so we do not need to serve anything from flask's end

if __name__ == "__main__":
    #start app
    Flask.run(app, host="0.0.0.0", port=5000)
