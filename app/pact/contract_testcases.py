import sys
sys.path.insert(0, '../../')
sys.path.insert(1, '../')
sys.path.insert(1, '/')

from pact import Consumer, Provider, Like
from parameterized import parameterized
import atexit
import unittest
import requests
import sys
import os
import json


#PACT_MOCK_HOST = 'localhost'
#PACT_MOCK_PORT = 5053

PACT_MOCK_HOST = 'localhost'
#PACT_MOCK_HOST = 'localhost'
PACT_MOCK_PORT = '5080'

pact = Consumer('GUI').has_pact_with(Provider('Rules'), host_name=PACT_MOCK_HOST, port=PACT_MOCK_PORT)
pact.start_service()
atexit.register(pact.stop_service)

# setting up path for pact file
CURR_FILE_PATH = os.path.dirname(os.path.abspath(__file__))
PACT_DIR = os.path.join(CURR_FILE_PATH + '/pacts/', '')
PACT_FILE = os.path.join(PACT_DIR, 'archiv/pact.json')


# Defining Class
class verifyKunden(unittest.TestCase):

    @parameterized.expand([
        ['2', '1', 'Name', 'Vorname', 'Strasse', '12345', 'Ort', '1999-01-17', 'ok', 'Prüfungen erfolgreich'],
        ['x', '1', 'Name', 'Vorname', 'Strasse', '12345', 'Ort', '1999-01-17', 'nok', 'Ungültiger Wert in Feld \'Rolle\''],
        ['2', '1', 'Name', 'Vorname', 'Strasse', 'xxxxx', 'Ort', '1999-01-17', 'nok', 'PLZ nicht numerisch'],
        ['2', '1', 'Name', 'Vorname', 'Strasse', 'xxxxx', 'Ort', '2009-01-17', 'nok', 'Alter falsch']
    ])
    def test_kunde_anlegen(self, rolle, anrede, name, vorname, strasse, plz, ort, geburtsdatum, status, rc):
        # Platzhalter für Methodenaufruf zur Erzeugung des Payloads
        payload = {
         'kunde_id': '',
         'rolle': rolle,
         'anrede': anrede,
         'name': name,
         'vorname': vorname,
         'strasse': strasse,
         'plz': plz,
         'ort': ort,
         'geburtsdatum': geburtsdatum}



        expected = {
            "status": { 'result': status,
                        'rc': rc}
        }

        # Consumer Request und erwarteter Response
        (pact
            .given('Testfall für ' + rc)
            .upon_receiving('Erzeugen eines Response mit Rueckmeldung: ', rc)
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