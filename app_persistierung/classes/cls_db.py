import sys
sys.path.insert(0, '/')
sys.path.insert(1, '../../')
import mysql.connector
import mysql.connector
from configparser import ConfigParser

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
        config = ConfigParser()
        config.read('config/config.ini')
        if config.get('Service Mock', 'mock') != "True":
            ziel = 'mysql Datenbank'
        else:
            ziel = 'mysql Datenbank Mock'
        configuration = {
            'user': config.get(ziel, 'user'),
            'password': config.get(ziel, 'pass'),
            'host': config.get(ziel, 'host'),
            'port': config.get(ziel, 'port'),
            'database': config.get(ziel, 'database')
        }
        connection = mysql.connector.connect(**configuration)
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

    def updateKunde(self, dictKunde):
        sql = "UPDATE kunden " \
              "SET rolle_id = %s, " \
              "anrede = %s, " \
              "name = %s, " \
              "vorname = %s, " \
              "strasse = %s, " \
              "plz = %s, " \
              "ort = %s " \
              "where kunde_id = %s"
        val = (dictKunde['rolle'], dictKunde['anrede'], dictKunde['name'], dictKunde['vorname'], dictKunde['strasse'],
               dictKunde['plz'], dictKunde['ort'], dictKunde['kunde_id'])
        connection = self.conn()
        cursor = connection.cursor()
        cursor.execute(sql, val)
        kunde_id = cursor.lastrowid
        connection.commit()
        cursor.close()
        connection.close()
        return kunde_id

    def viewKunde(self, dictKunde):
        sql = "SELECT * FROM kunden where kunde_id = " + dictKunde['kunde_id']
        connection = self.conn()
        cursor = connection.cursor()
        cursor.execute(sql)
        kunde_id = cursor.lastrowid
        connection.commit()
        cursor.close()
        connection.close()
        return kunde_id


