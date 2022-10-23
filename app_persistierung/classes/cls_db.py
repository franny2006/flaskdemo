import sys
sys.path.insert(0, '/')
sys.path.insert(1, '../../')
import mysql.connector
import mysql.connector
from configparser import ConfigParser
import json

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

    def getKunden(self):
        sql = "SELECT * FROM kunden order by kunde_id"
        connection = self.conn()
        cursor = connection.cursor()
        cursor.execute(sql)
        row_headers = [x[0] for x in cursor.description]  # this will extract row headers
        rv = cursor.fetchall()
        json_data = []
        for result in rv:
            json_data.append(dict(zip(row_headers, result)))
        data = json.dumps(json_data, default=str)
        data = json.loads(data)
        return data

    def addKunde(self, dictKunde):
        sql = "INSERT INTO kunden (rolle_id, anrede, name, vorname, strasse, plz, ort, geburtsdatum) VALUES (%s, %s, %s, %s, %s, %s, %s, %s)"
        val = (dictKunde['rolle'], dictKunde['anrede'], dictKunde['name'], dictKunde['vorname'], dictKunde['strasse'],
               dictKunde['plz'], dictKunde['ort'], dictKunde['geburtsdatum'])
        connection = self.conn()
        cursor = connection.cursor()
        cursor.execute(sql, val)
        kunde_id = cursor.lastrowid
        connection.commit()
        cursor.close()
        connection.close()
        return kunde_id

    def updateKunde(self, dictKunde):
        print(dictKunde)
        sql = "UPDATE kunden " \
              "SET rolle_id = %s, " \
              "anrede = %s, " \
              "name = %s, " \
              "vorname = %s, " \
              "strasse = %s, " \
              "plz = %s, " \
              "ort = %s, " \
              "geburtsdatum = %s " \
              "where kunde_id = %s"
        val = (dictKunde['rolle'], dictKunde['anrede'], dictKunde['name'], dictKunde['vorname'], dictKunde['strasse'],
               dictKunde['plz'], dictKunde['ort'], dictKunde['geburtsdatum'], dictKunde['kunde_id'])
        connection = self.conn()
        cursor = connection.cursor()
        cursor.execute(sql, val)
        kunde_id = cursor.lastrowid
        connection.commit()
        cursor.close()
        connection.close()
        return kunde_id

    def getKunde(self, kunde_id):
        sql = "SELECT * FROM kunden where kunde_id = " + kunde_id
        connection = self.conn()
        cursor = connection.cursor()
        cursor.execute(sql)
        row_headers = [x[0] for x in cursor.description]  # this will extract row headers
        rv = cursor.fetchall()
        json_data = []
        for result in rv:
            json_data.append(dict(zip(row_headers, result)))
        data = json.dumps(json_data, default=str)
        data = json.loads(data)
        return data

    def getKundenNamen(self):
        sql = "select kunde_id, name, vorname from kunden"
        connection = self.conn()
        cursor = connection.cursor()
        cursor.execute(sql)
        row_headers = [x[0] for x in cursor.description]  # this will extract row headers
        rv = cursor.fetchall()
        nameList = []
        for row in rv:
            kunde = {}
            kunde['value'] = row[0]
            kunde['label'] = row[1] + ", " + row[2]
            nameList.append(kunde)
        return nameList

    def getHsn(self):
        sql = "SELECT distinct hersteller, hsn FROM kfz_typen"
        connection = self.conn()
        cursor = connection.cursor()
        cursor.execute(sql)
        row_headers = [x[0] for x in cursor.description]  # this will extract row headers
        rv = cursor.fetchall()
        json_data = []
        herstellerList = []
        for row in rv:
            hersteller = {}
            hersteller['label'] = row[0]
            hersteller['value'] = row[1]
            herstellerList.append(hersteller)
        return herstellerList

    def getTsn(self):
        sql = "SELECT distinct modell, tsn, anzahl FROM kfz_typen"
        connection = self.conn()
        cursor = connection.cursor()
        cursor.execute(sql)
        row_headers = [x[0] for x in cursor.description]  # this will extract row headers
        rv = cursor.fetchall()
        json_data = []
        herstellerList = []
        for row in rv:
            hersteller = {}
            hersteller['label'] = row[0] + ", " + row[1] + ", (Anz. Zulassungen: " + row[2] + ")"
            hersteller['value'] = row[1]
            herstellerList.append(hersteller)
        return herstellerList

    def addOffer(self, dictOffer):
        sql = "INSERT INTO antraege (kunde_id, fuehrerschein, hsn, tsn, kategorie, ez, fahrleistung, verwendung, vers_beginn) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s)"
        val = (dictOffer['kunde_id'], dictOffer['fuehrerschein'], dictOffer['hsn'], dictOffer['tsn'], dictOffer['kategorie'], dictOffer['ez'],
               dictOffer['fahrleistung'], dictOffer['verwendung'], dictOffer['vers_beginn'])
        connection = self.conn()
        cursor = connection.cursor()
        cursor.execute(sql, val)
        angebot_id = cursor.lastrowid
        connection.commit()
        cursor.close()
        connection.close()
        return angebot_id

    def getOffers(self):
        sql = "SELECT * FROM kunden k, antraege a where a.kunde_id = k.kunde_id order by antrag_id"
        connection = self.conn()
        cursor = connection.cursor()
        cursor.execute(sql)
        row_headers = [x[0] for x in cursor.description]  # this will extract row headers
        rv = cursor.fetchall()
        json_data = []
        for result in rv:
            json_data.append(dict(zip(row_headers, result)))
        data = json.dumps(json_data, default=str)
        data = json.loads(data)
        return data

    def getOffer(self, offerId):
        sql = "SELECT * FROM kunden k, antraege a where antrag_id = " + offerId + " and a.kunde_id = k.kunde_id order by antrag_id"
        connection = self.conn()
        cursor = connection.cursor()
        cursor.execute(sql)
        row_headers = [x[0] for x in cursor.description]  # this will extract row headers
        rv = cursor.fetchall()
        json_data = []
        for result in rv:
            json_data.append(dict(zip(row_headers, result)))
        data = json.dumps(json_data, default=str)
        data = json.loads(data)
        return data


