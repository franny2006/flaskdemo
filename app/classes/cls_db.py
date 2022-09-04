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



