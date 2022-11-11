from behave import *
import requests
import json
import sys
from datetime import date, datetime
import re
from datetime import date, datetime, timedelta
sys.path.insert(0, '../../')


@given('Über die Schnittstelle kommt ein geprüfter Auftrag zur Kundenanlage')
def step_impl(context):
    pass

@when('der Kunde hat die Rolle {rolle}')
def step_Rolle(context, rolle):
    context.rolle = rolle
 #   context.dictPayload['rolle'] = rolle

 #   assert context.rolle == "9"

@when('der Kunde hat die Anrede {anrede}')
def step_Anrede(context, anrede):
    context.anrede = anrede
 #   context.dictPayload['rolle'] = rolle

@when('der Kunde hat den Vornamen {vorname}')
def step_Vorname(context, vorname):
    context.vorname = vorname

@when('der Kunde hat den Namen {name}')
def step_Name(context, name):
    context.name = name

@when('der Kunde wohnt in Strasse {strasse}')
def step_strasse(context, strasse):
    context.strasse = strasse

@when('der Kunde wohnt in PLZ {plz}')
def step_plz(context, plz):
    context.plz = plz

@when('der Kunde wohnt in Ort {ort}')
def step_Ort(context, ort):
    context.ort = ort

@when('der Kunde ist geboren am {geburtsdatum}')
def step_Geburtsdatum(context, geburtsdatum):
    context.geburtsdatum = geburtsdatum

    date_format = '%Y-%m-%d'
    try:
        geburtstag = datetime.strptime(geburtsdatum, date_format)
        geburtsdatumKonkret = geburtstag.date()
    except:
        regel = re.split(r'\s', geburtsdatum)

        if regel[0].lower() == 'heute':
            referenzdatum = date.today()
        elif regel[0].lower() == 'gestern':
            referenzdatum = date.today() - timedelta(days=1)
        elif regel[0].lower() == 'morgen':
            referenzdatum = date.today() + timedelta(days=1)

        if regel[1] == "-":
            if regel[3].lower() == 'y':
                geburtsdatumKonkret = datetime(referenzdatum.year - int(regel[2]), referenzdatum.month, referenzdatum.day)
                geburtsdatumKonkret = geburtsdatumKonkret.date()
            elif regel[3].lower() == 'w':
                geburtsdatumKonkret = referenzdatum - timedelta(weeks=int(regel[2]))
            elif regel[3].lower() == 'd':
                geburtsdatumKonkret = referenzdatum - timedelta(days=int(regel[2]))
        elif regel[1] == "+":
            if regel[3].lower() == 'y':
                geburtsdatumKonkret = datetime(referenzdatum.year + int(regel[2]), referenzdatum.month, referenzdatum.day)
                geburtsdatumKonkret = geburtsdatumKonkret.date()
            elif regel[3].lower() == 'w':
                geburtsdatumKonkret = referenzdatum + timedelta(months=int(regel[2]))
            elif regel[3].lower() == 'd':
                geburtsdatumKonkret = referenzdatum + timedelta(days=int(regel[2]))

    context.geburtsdatumKonkret = geburtsdatumKonkret



@then('der Kunde wurde erfolgreich in der Datenbank gespeichert')
def step_Response(context):

    url = 'http://127.0.0.1:5005/api/v1.0/addKunde'
    payload = {
        'rolle': '' + context.rolle + '',
        'anrede': '' + context.anrede + '',
        'name': '' + context.name + '',
        'vorname': '' + context.vorname + '',
        'strasse': '' + context.strasse + '',
        'plz': '' + context.plz + '',
        'ort': '' + context.ort + '',
        'geburtsdatum': '' + str(context.geburtsdatumKonkret) + ''}
    jsonPayload = json.dumps(payload, default=str)
    jsonPayload = json.loads(jsonPayload)
    response = requests.post(url, json=jsonPayload)
    data = response.json()
    print(data)
 #   print("Response: ", data['status']['result'], data['status']['rc'])
    kundeGespeichert = data['kunde']
    assert data['kunde']['name'] == context.name, f"Kunde konnte nicht gespeichert werden"
