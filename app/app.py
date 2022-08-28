from typing import List, Dict
from flask import Flask
import mysql.connector
import json

from cls_db import cls_dbAktionen

app = Flask(__name__)





def test_table() -> List[Dict]:
    config = {
        'user': 'root',
        'password': 'root',
        'host': 'db',
        'port': '3306',
        'database': 'devopsroles'
    }
    connection = mysql.connector.connect(**config)
    cursor = connection.cursor()
    cursor.execute('SELECT * FROM test_table')
    results = [{name: color} for (name, color) in cursor]
    cursor.close()
    connection.close()

    return results


@app.route('/')
def index() -> str:
    statement = "SELECT * FROM test_table"
    db = cls_dbAktionen()
    results = db.execSelect(statement)
    print(results)
    results = [{name: color} for (name, color) in results]
    return json.dumps({'test_table': results})


if __name__ == '__main__':
    app.run(host='0.0.0.0')