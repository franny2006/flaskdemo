from typing import List, Dict
from flask import Flask, request, jsonify, render_template, redirect, flash, jsonify, abort

import mysql.connector
import json
import requests

from classes.cls_db import cls_dbAktionen
from classes.cls_verwaltung import cls_verwaltung
from forms import KundeForm, OfferForm

from configparser import ConfigParser
config = ConfigParser()
config.read('config/config.ini')

app = Flask(__name__)
app.config["DEBUG"] = True
app.config['SECRET_KEY'] = 'you-will-never-guess'




def test_table() -> List[Dict]:
    config = {
        'user': 'root',
        'password': 'root',
        'host': 'db',
        'port': '3306',
        'database': 'devopsroles'
    }
    connection = mysql.connector.connect(**config)
    cursor = connection.cursor()
    cursor.execute('SELECT * FROM test_table')
    results = [{name: color} for (name, color) in cursor]
    cursor.close()
    connection.close()

    return results

@app.route('/', methods=['GET'])
def home():
    return "<h1>Demoanwendung</h1>" \
           "<h3>Komponente Oberfläche</h3>"

@app.route('/viewKunden')
def index() -> str:
    headers = {'Content-type': 'application/json'}
    if config.get('Service Mock', 'mock') != "True":
        url_rules = "http://" + config.get('Service Regelengine', 'host') + ":" + config.get('Service Regelengine', 'port')
        url_persist = "http://" + config.get('Service Persistierung', 'host') + ":" + config.get('Service Persistierung', 'port')
    else:
        url_rules = "http://" + config.get('Service Regelengine Mock', 'host') + ":" + config.get('Service Regelengine Mock', 'port')
        url_persist = "http://" + config.get('Service Persistierung Mock', 'host') + ":" + config.get('Service Persistierung Mock', 'port')

    r = requests.post(url_persist + '/api/v1.0/getKunden', headers=headers)
    data = r.json()
 #   data = json.loads(data)
    print(data)
    return render_template('index.html', title='Index', data=data)


@app.route('/test_db')
def test_db():
    verwaltung = cls_verwaltung()
    payload = verwaltung.readDb()
    print(payload)
    return render_template('base.html')


@app.route('/addKunde', methods=['GET', 'POST'])
def addKunde():
    # Formulardaten vorbereiten
    form = KundeForm()

    # Verarbeitung, wenn Formular validiert werden kann
    if form.validate_on_submit():
        payload = {
            'rolle': form.kundeRolle.data,
            'anrede': form.kundeAnrede.data,
            'name': form.kundeName.data,
            'vorname': form.kundeVorname.data,
            'strasse': form.kundeStrasse.data,
            'plz': form.kundePlz.data,
            'ort': form.kundeOrt.data,
            'geburtsdatum': form.kundeGeburtsdatum.data.isoformat()
        }
        headers = {'Content-type': 'application/json'}
     #   r = requests.post('http://localhost:5010/api/v1/resources/verifyKunde', json=payload, headers=headers)
        if config.get('Service Mock', 'mock') != "True":
            url_rules = "http://"+config.get('Service Regelengine', 'host') + ":" + config.get('Service Regelengine', 'port')
            url_persist = "http://" + config.get('Service Persistierung', 'host') + ":" + config.get('Service Persistierung', 'port')
        else:
            url_rules = "http://" + config.get('Service Regelengine Mock', 'host') + ":" + config.get('Service Regelengine Mock', 'port')
            url_persist = "http://" + config.get('Service Persistierung Mock', 'host') + ":" + config.get('Service Persistierung Mock', 'port')

        r = requests.post(url_rules + '/api/v1/resources/verifyKunde', json=payload, headers=headers)
        flash('Daten gespeichert für Kunde {} {}'.format(
            form.kundeVorname.data, form.kundeName.data))
        dict_status = r.json()

        print("Status Aufruf: ", dict_status)
        if 'nok' in dict_status['status']['result']:
            flash('Fehler bei {} {}: {}'.format(form.kundeVorname.data, form.kundeName.data, dict_status['status']))
        else:
            r = requests.post(url_persist + '/api/v1.0/addKunde', json=payload, headers=headers)
            return redirect('/viewKunden')
    return render_template('addKunde.html', title='Kunde anlegen', form=form)




@app.route('/modifyKunde', methods=['GET', 'POST'])
def modifyKunde():

    kunde_id = request.args.get('kunde_id')

    payload = {
        'kunde_id': kunde_id
    }
    headers = {
        'Content-type': 'application/json'}

    if config.get('Service Mock', 'mock') != "True":
        url_rules = "http://" + config.get('Service Regelengine', 'host') + ":" + config.get('Service Regelengine', 'port')
        url_persist = "http://" + config.get('Service Persistierung', 'host') + ":" + config.get('Service Persistierung', 'port')
    else:
        url_rules = "http://" + config.get('Service Regelengine Mock', 'host') + ":" + config.get('Service Regelengine Mock', 'port')
        url_persist = "http://" + config.get('Service Persistierung Mock', 'host') + ":" + config.get('Service Persistierung Mock', 'port')

    r = requests.post(url_persist + '/api/v1.0/getKunde', json=payload, headers=headers)
    data = r.json()

    print("Ergebnis getKunde: ", r, data)

    form = KundeForm(kundeAnrede=str(data['kunde'][0]['anrede']), kundeRolle=str(data['kunde'][0]['rolle_id']))
 #   form.kundeAnrede.data = str(data['kunde'][0]['anrede'])
 #   form.kundeRolle.data = str(data['kunde'][0]['rolle_id'])
    form.kunde_id.data = kunde_id
    #  return json.dumps({'test_table': results})
    # Verarbeitung, wenn Formular validiert werden kann
    if form.validate_on_submit():
        payload = {
            'kunde_id': form.kunde_id.data,
            'rolle': form.kundeRolle.data,
            'anrede': form.kundeAnrede.data,
            'name': form.kundeName.data,
            'vorname': form.kundeVorname.data,
            'strasse': form.kundeStrasse.data,
            'plz': form.kundePlz.data,
            'ort': form.kundeOrt.data,
            'geburtsdatum': form.kundeGeburtsdatum.data.isoformat()
        }
        print(payload)

        r = requests.post(url_rules + '/api/v1/resources/verifyKunde', json=payload, headers=headers)
        flash('Daten gespeichert für Kunde {} {}'.format(
            form.kundeVorname.data, form.kundeName.data))
        dict_status = r.json()

        print("Status Aufruf: ", dict_status)
        if 'nok' in dict_status['status']['result']:
            flash('Fehler bei {} {}: {}'.format(form.kundeVorname.data, form.kundeName.data, dict_status['status']))
        else:
            r = requests.post(url_persist + '/api/v1.0/updateKunde', json=payload, headers=headers)
            return redirect('/viewKunden')
    return render_template('modifyKunde.html', title='Kunde bearbeiten', form=form, data=data)


@app.route('/addOffer', methods=['GET', 'POST'])
def addOffer():
    if config.get('Service Mock', 'mock') != "True":
        url_rules = "http://" + config.get('Service Regelengine', 'host') + ":" + config.get('Service Regelengine', 'port')
        url_persist = "http://" + config.get('Service Persistierung', 'host') + ":" + config.get('Service Persistierung', 'port')
    else:
        url_rules = "http://" + config.get('Service Regelengine Mock', 'host') + ":" + config.get('Service Regelengine Mock', 'port')
        url_persist = "http://" + config.get('Service Persistierung Mock', 'host') + ":" + config.get('Service Persistierung Mock', 'port')

    form = OfferForm()

    headers = {
        'Content-type': 'application/json'}
    # Verarbeitung, wenn Formular validiert werden kann
    if form.validate_on_submit():
        if form.angebotKundeId.data == "":
            form.angebotKundeId.data = "999"
        payload = {
            'kunde_id': form.angebotKundeId.data,
            'fuehrerschein': form.angebotFuehrerschein.data.isoformat(),
            'hsn': form.angebotHsn.data,
            'tsn': form.angebotTsn.data,
            'kategorie': form.angebotKategorie.data,
            'ez': form.angebotErstzulassung.data.isoformat(),
            'fahrleistung': form.angebotKilometer.data,
            'verwendung': form.angebotVerwendung.data,
            'vers_beginn': form.angebotVersicherungsbeginn.data.isoformat()
        }
        print(payload)

        r = requests.post(url_rules + '/api/v1/resources/verifyOffer', json=payload, headers=headers)
        dict_status = r.json()
        print("Status Prüfungen Offer: ", dict_status)
        flash('Daten gespeichert für Kunde {} {}'.format(
            form.angebotKundeVorname.data, form.angebotKundeName.data))
  #      dict_status = r.json()
        print("Status Aufruf: ", dict_status)
        if 'nok' in dict_status['status']['result']:
            flash('Fehler bei {} {}: {}'.format(form.angebotKundeVorname.data, form.angebotKundeName.data, dict_status['status']))
        else:
            r = requests.post(url_persist + '/api/v1.0/addOffer', json=payload, headers=headers)
            return redirect('/viewOffers')
    return render_template('addOffer.html', title='Angebot erstellen', form=form)



@app.route('/createOffer', methods=['GET', 'POST'])
def createOffer():
    if config.get('Service Mock', 'mock') != "True":
        url_rules = "http://" + config.get('Service Regelengine', 'host') + ":" + config.get('Service Regelengine', 'port')
        url_persist = "http://" + config.get('Service Persistierung', 'host') + ":" + config.get('Service Persistierung', 'port')
    else:
        url_rules = "http://" + config.get('Service Regelengine Mock', 'host') + ":" + config.get('Service Regelengine Mock', 'port')
        url_persist = "http://" + config.get('Service Persistierung Mock', 'host') + ":" + config.get('Service Persistierung Mock', 'port')


    kunde_id = request.args.get('kunde_id')

    payload = {
        'kunde_id': kunde_id
    }
    headers = {
        'Content-type': 'application/json'}



    r = requests.post(url_persist + '/api/v1.0/getKunde', json=payload, headers=headers)
    data = r.json()

    print("Ergebnis getKunde: ", r, data)

    form = OfferForm()
 #   form.kundeAnrede.data = str(data['kunde'][0]['anrede'])
 #   form.kundeRolle.data = str(data['kunde'][0]['rolle_id'])
    form.angebotKundeId.data = kunde_id
    #  return json.dumps({'test_table': results})
    # Verarbeitung, wenn Formular validiert werden kann
    if form.validate_on_submit():
        payload = {
            'kunde_id': form.angebotKundeId.data,
            'name': form.angebotKundeName.data,
            'vorname': form.angebotKundeVorname.data,
            'strasse': form.angebotKundeStrasse.data,
            'plz': form.angebotKundePlz.data,
            'ort': form.angebotKundeOrt.data
        }
        print(payload)

   #     r = requests.post(url_rules + '/api/v1/resources/verifyKunde', json=payload, headers=headers)
        flash('Daten gespeichert für Kunde {} {}'.format(
            form.angebotKundeVorname.data, form.angebotKundeName.data))
        dict_status = r.json()

        print("Status Aufruf: ", dict_status)
        if 'nok' in dict_status['status']['result']:
            flash('Fehler bei {} {}: {}'.format(form.angebotKundeVorname.data, form.angebotKundeName.data, dict_status['status']))
        else:
            r = requests.post(url_persist + '/api/v1.0/addOffer', json=payload, headers=headers)
            return redirect('/viewKunden')
    return render_template('addOffer.html', title='Kunde bearbeiten', form=form, data=data)

@app.route('/listKundenNamen')
def listKundenNamen():
    print("Kundennamen Aufruf")
    if config.get('Service Mock', 'mock') != "True":
        url_rules = "http://" + config.get('Service Regelengine', 'host') + ":" + config.get('Service Regelengine', 'port')
        url_persist = "http://" + config.get('Service Persistierung', 'host') + ":" + config.get('Service Persistierung', 'port')
    else:
        url_rules = "http://" + config.get('Service Regelengine Mock', 'host') + ":" + config.get('Service Regelengine Mock', 'port')
        url_persist = "http://" + config.get('Service Persistierung Mock', 'host') + ":" + config.get('Service Persistierung Mock', 'port')

    headers = {'Content-type': 'application/json'}
    r = requests.post(url_persist + '/api/v1.0/getKundenNamen', headers=headers)
    data = r.json()
    print("Kundennamen: ", data['kundenNamen'])
    return jsonify(data['kundenNamen'])


@app.route('/viewKunde', methods=['GET', 'POST'])
def viewKunde():

    kunde_id = request.args.get('kunde_id')

    payload = {
        'kunde_id': kunde_id
    }
    headers = {
        'Content-type': 'application/json'}

    if config.get('Service Mock', 'mock') != "True":
        url_rules = "http://" + config.get('Service Regelengine', 'host') + ":" + config.get('Service Regelengine', 'port')
        url_persist = "http://" + config.get('Service Persistierung', 'host') + ":" + config.get('Service Persistierung', 'port')
    else:
        url_rules = "http://" + config.get('Service Regelengine Mock', 'host') + ":" + config.get('Service Regelengine Mock', 'port')
        url_persist = "http://" + config.get('Service Persistierung Mock', 'host') + ":" + config.get('Service Persistierung Mock', 'port')

    r = requests.post(url_persist + '/api/v1.0/getKunde', json=payload, headers=headers)
    data = r.json()
    return jsonify(data['kunde'])


@app.route('/listHsn')
def listHsn():

    if config.get('Service Mock', 'mock') != "True":
        url_rules = "http://" + config.get('Service Regelengine', 'host') + ":" + config.get('Service Regelengine', 'port')
        url_persist = "http://" + config.get('Service Persistierung', 'host') + ":" + config.get('Service Persistierung', 'port')
    else:
        url_rules = "http://" + config.get('Service Regelengine Mock', 'host') + ":" + config.get('Service Regelengine Mock', 'port')
        url_persist = "http://" + config.get('Service Persistierung Mock', 'host') + ":" + config.get('Service Persistierung Mock', 'port')

    headers = {'Content-type': 'application/json'}
    r = requests.post(url_persist + '/api/v1.0/getHsn', headers=headers)
    data = r.json()
    print("Hsn: ", data['hersteller'][0])
    return jsonify(data['hersteller'])

@app.route('/listTsn')
def listTsn():

    if config.get('Service Mock', 'mock') != "True":
        url_rules = "http://" + config.get('Service Regelengine', 'host') + ":" + config.get('Service Regelengine', 'port')
        url_persist = "http://" + config.get('Service Persistierung', 'host') + ":" + config.get('Service Persistierung', 'port')
    else:
        url_rules = "http://" + config.get('Service Regelengine Mock', 'host') + ":" + config.get('Service Regelengine Mock', 'port')
        url_persist = "http://" + config.get('Service Persistierung Mock', 'host') + ":" + config.get('Service Persistierung Mock', 'port')

    headers = {'Content-type': 'application/json'}
    r = requests.post(url_persist + '/api/v1.0/getTsn', headers=headers)
    data = r.json()
    print("Tsn: ", data['hersteller'][0])
    return jsonify(data['hersteller'])


@app.route('/viewOffers')
def viewOffers() -> str:
    headers = {'Content-type': 'application/json'}
    if config.get('Service Mock', 'mock') != "True":
        url_rules = "http://" + config.get('Service Regelengine', 'host') + ":" + config.get('Service Regelengine', 'port')
        url_persist = "http://" + config.get('Service Persistierung', 'host') + ":" + config.get('Service Persistierung', 'port')
    else:
        url_rules = "http://" + config.get('Service Regelengine Mock', 'host') + ":" + config.get('Service Regelengine Mock', 'port')
        url_persist = "http://" + config.get('Service Persistierung Mock', 'host') + ":" + config.get('Service Persistierung Mock', 'port')

    r = requests.post(url_persist + '/api/v1.0/getOffers', headers=headers)
    data = r.json()
 #   data = json.loads(data)
    print(data)
    return render_template('antraege.html', title='Index', data=data)

@app.route('/viewOffer', methods=['GET', 'POST'])
def viewOffer():

    antrag_id = request.args.get('antrag_id')

    payload = {
        'antrag_id': antrag_id
    }
    headers = {
        'Content-type': 'application/json'}

    if config.get('Service Mock', 'mock') != "True":
        url_rules = "http://" + config.get('Service Regelengine', 'host') + ":" + config.get('Service Regelengine', 'port')
        url_persist = "http://" + config.get('Service Persistierung', 'host') + ":" + config.get('Service Persistierung', 'port')
    else:
        url_rules = "http://" + config.get('Service Regelengine Mock', 'host') + ":" + config.get('Service Regelengine Mock', 'port')
        url_persist = "http://" + config.get('Service Persistierung Mock', 'host') + ":" + config.get('Service Persistierung Mock', 'port')

    r = requests.post(url_persist + '/api/v1.0/getOffer', json=payload, headers=headers)
    data = r.json()

    return render_template('viewAntrag.html', title='Angebot', data=data['offer'])


if __name__ == '__main__':
    app.run(host='0.0.0.0')