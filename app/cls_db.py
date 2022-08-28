import sys
sys.path.insert(0, '/')
sys.path.insert(1, '../../')
import mysql.connector

class cls_dbAktionen():
    def __init__(self):
        config = {
            'user': 'root',
            'password': 'root',
            'host': 'db',
            'port': '3306',
            'database': 'devopsroles'
        }
        self.connection = mysql.connector.connect(**config)

    def execSql(self, statement, val):
    #    print("SQL-Exec: ", statement, val)

        try:
            cur = self.connection.cursor()
        except:
            print("Fehler")


    def execSelect(self, statement):
        #print("SQL-Select: ", statement, val, art)
        result = []

        try:
            cursor = self.connection.cursor()
            results = cursor.execute(statement)
            cursor.close()
            self.connection.close()
        except:
            print("Fehler bei Select")
            results = ""

        return results

