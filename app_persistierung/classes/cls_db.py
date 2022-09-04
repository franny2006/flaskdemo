import sys
sys.path.insert(0, '/')
sys.path.insert(1, '../../')
import mysql.connector

class cls_dbAktionen():
    def __init__(self):
        pass

    def conn(self):
        # config = {
        #     'user': 'test',
        #     'password': 'test',
        #     'host': 'localhost',
        #     'port': '3306',
        #     'database': 'devopsroles'
        # }
        # config = {
        #     'user': 'root',
        #     'password': 'root',
        #     'host': 'db',
        #     'port': '3306',
        #     'database': 'devopsroles'
        # }
        config = {
            'user': 'test',
            'password': 'test',
            'host': 'localhost',
            'port': '3306',
            'database': 'devopsroles'
        }
        connection = mysql.connector.connect(**config)
        return connection

    def addKunde(self, dictKunde):
        sql = "INSERT INTO kunden (rolle_id, anrede, name, vorname, strasse, plz, ort) VALUES (%s, %s, %s, %s, %s, %s, %s)"
        val = (dictKunde['rolle'], dictKunde['anrede'], dictKunde['name'], dictKunde['vorname'], dictKunde['strasse'],
               dictKunde['plz'], dictKunde['ort'])
        connection = self.conn()
        cursor = connection.cursor()
        cursor.execute(sql, val)
        kunde_id = cursor.lastrowid
        connection.commit()
        cursor.close()
        connection.close()
        return kunde_id


