import sys
sys.path.insert(0, '../../')
sys.path.insert(1, '../')
sys.path.insert(1, '/')

from pact import Consumer, Provider
import atexit
import unittest
import requests
import sys
import os
import json

pact = Consumer('GUI').has_pact_with(Provider('Rules'), host_name='Mockservice Rules', port=1234)
pact.start_service()
atexit.register(pact.stop_service)

# setting up path for pact file
CURR_FILE_PATH = os.path.dirname(os.path.abspath(__file__))
PACT_DIR = os.path.join(CURR_FILE_PATH + '/pacts/', '')
PACT_FILE = os.path.join(PACT_DIR, 'archiv/pact.json')


# Defining Class
class verifyKunden(unittest.TestCase):

    def test_kunde_anlegen(self):
        # Platzhalter für Methodenaufruf zur Erzeugung des Payloads
        payload = {
            'kunde_id': '',
            'rolle': '2',
            'anrede': '1',
            'name': 'CT_1_Name',
            'vorname': 'CT_1_Vorname',
            'strasse': 'CT_1_Strasse',
            'plz': 'CT_1_Plz',
            'ort': 'CT_1_Ort',
            'geburtsdatum': '01-01-2010'
        }
   #     payload = json.loads(payload)


        expected = {
                "status": { 'result': 'ok',
                            'rc': 'Prüfungen erfolgreich'}
             }

        # Consumer Request und erwarteter Response
        (pact
         .given('Request an Regelengine mit gültigem Auftrag zur Kundenanlage')
         .upon_receiving('Erzeugen eines Response mit positivem Prüfergebnis')
         .with_request(method = 'POST',
                       path = '/api/v1/resources/verifyKunde',
                       body = payload,
                       headers = {"Content-Type": "application/json"})
         .will_respond_with(200, body=expected))


        headers = {"Content-Type": "application/json"}



        with pact:
            result = requests.post(pact.uri + '/api/v1/resources/verifyKunde', json=payload, headers=headers)

        self.assertEqual(result.json(), expected)
        pact.verify()