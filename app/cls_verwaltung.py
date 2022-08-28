from .cls_db import cls_dbAktionen
import json


class cls_auftragsverwaltung():
    def __init__(self):
        self.db = cls_dbAktionen()
   #     self.readAuftraege()

    def readAuftraege(self):
        sql_auftraege = "select runId, panr, prnr, voat, zw, zlzr, SA_11_zgep, SA_13_ort from V_Testview"
        result = self.db.execSelect(sql_auftraege, '', art='fetchall')

        payload = json.dumps([dict(ix) for ix in result])
        print(payload)

        return payload

    def readAuftragsdetails(self, runId, panr, prnr):
        sql_auftrag = "select * from V_Testview where runId = '" + runId + "' and panr = '" + panr + "' and prnr = '" + prnr + "'"
        result = self.db.execSelect(sql_auftrag, '', art='fetchall')

        payload = json.dumps([dict(ix) for ix in result])

        return payload