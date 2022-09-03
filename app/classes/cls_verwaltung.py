from cls_db import cls_dbAktionen
import json


class cls_verwaltung():
    def __init__(self):
        self.db = cls_dbAktionen()
   #     self.readAuftraege()

    def readDb(self):
        sql_auftraege = "select * from test_table"
        db = cls_dbAktionen()
        connection = db.conn()
        cursor = connection.cursor()
        cursor.execute('SELECT * FROM test_table')
        row_headers = [x[0] for x in cursor.description]  # this will extract row headers
        rv = cursor.fetchall()
        json_data = []
        for result in rv:
            json_data.append(dict(zip(row_headers, result)))

        print(json_data)

        return json_data

    def readAuftragsdetails(self, runId, panr, prnr):
        sql_auftrag = "select * from V_Testview where runId = '" + runId + "' and panr = '" + panr + "' and prnr = '" + prnr + "'"
        result = self.db.execSelect(sql_auftrag, '', art='fetchall')

        payload = json.dumps([dict(ix) for ix in result])

        return payload