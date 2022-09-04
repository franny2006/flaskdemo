import sys
sys.path.insert(0, '/')
sys.path.insert(1, '../../')
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





