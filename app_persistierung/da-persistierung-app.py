from typing import List, Dict
from flask import Flask, request, jsonify, render_template, redirect, flash, jsonify, abort
import mysql.connector
import json
import requests

from classes.cls_db import cls_dbAktionen


app = Flask(__name__)
app.config["DEBUG"] = True
app.config['SECRET_KEY'] = 'you-will-never-guess'





@app.route('/', methods=['GET'])
def home():
    return "<h1>Demoanwendung</h1>" \
           "<h3>Komponente Persistierung</h3>"


@app.route('/api/v1.0/getKunden', methods=['POST'])
def getKunden():
    db = cls_dbAktionen()
    kunden = db.getKunden()
    return jsonify({'kunden': kunden}), 201

@app.route('/api/v1.0/addKunde', methods=['POST'])
def createKunde():
    if not request.json or not 'name' in request.json:
        abort(400)
    db = cls_dbAktionen()
    dictKunde = {
        'rolle': request.json['rolle'],
        'anrede': request.json['anrede'],
        'name': request.json['name'],
        'vorname': request.json.get('vorname', ""),
        'strasse': request.json.get('strasse', ""),
        'plz': request.json.get('plz', ""),
        'ort': request.json.get('ort', ""),
        'geburtsdatum': request.json.get('geburtsdatum', ""),
    }

    rowId = db.addKunde(dictKunde)
    return jsonify({'kunde': dictKunde}), 201
    #return rowId


@app.route('/api/v1.0/updateKunde', methods=['POST'])
def updateKunde():
    if not request.json or not 'kunde_id' in request.json:
        abort(400)
    db = cls_dbAktionen()
    dictKunde = {
        'rolle': request.json['rolle'],
        'anrede': request.json['anrede'],
        'name': request.json['name'],
        'vorname': request.json.get('vorname', ""),
        'strasse': request.json.get('strasse', ""),
        'plz': request.json.get('plz', ""),
        'ort': request.json.get('ort', ""),
        'kunde_id': request.json.get('kunde_id', ""),
        'geburtsdatum': request.json.get('geburtsdatum', ""),
    }

    rowId = db.updateKunde(dictKunde)
    return jsonify({'kunde': dictKunde}), 201
    #return rowId


@app.route('/api/v1.0/getKunde', methods=['POST'])
def getKunde():
    if not request.json or not 'kunde_id' in request.json:
        abort(400)
    db = cls_dbAktionen()
    print("kunde_id: ", request.json['kunde_id'])

    kunde = db.getKunde(request.json['kunde_id'])
    if len(kunde) == 0:
        abort(404)
    else:
        return jsonify({'kunde': kunde}), 201


@app.route('/api/v1.0/getKundenNamen', methods=['POST'])
def getKundenNamen():
    db = cls_dbAktionen()
    kundenNamen = db.getKundenNamen()
    return jsonify({'kundenNamen': kundenNamen}), 201

@app.route('/api/v1.0/getHsn', methods=['POST'])
def getHsn():
    db = cls_dbAktionen()
    hersteller = db.getHsn()
    return jsonify({'hersteller': hersteller}), 201


@app.route('/api/v1.0/getTsn', methods=['POST'])
def getTsn():
    db = cls_dbAktionen()
    hersteller = db.getTsn()
    return jsonify({'hersteller': hersteller}), 201


@app.route('/api/v1.0/addOffer', methods=['POST'])
def createOffer():
    print("ja")
    if not request.json or not 'kunde_id' in request.json:
        abort(400)
    db = cls_dbAktionen()

    if not request.json['kunde_id'] or request.json['kunde_id'] == '':
        request.json['kunde_id'] = '999'

    dictOffer = {
        'kunde_id': request.json['kunde_id'],
        'fuehrerschein': request.json.get('fuehrerschein'),
        'hsn': request.json['hsn'],
        'tsn': request.json['tsn'],
        'kategorie': request.json.get('kategorie'),
        'ez': request.json.get('ez'),
        'fahrleistung': request.json.get('fahrleistung'),
        'verwendung': request.json.get('verwendung'),
        'vers_beginn': request.json.get('vers_beginn'),
    }

    rowId = db.addOffer(dictOffer)
    return jsonify({'offer': dictOffer}), 201
    #return rowId

@app.route('/api/v1.0/getOffers', methods=['POST'])
def getOffers():
    db = cls_dbAktionen()
    offers = db.getOffers()
    return jsonify({'offers': offers}), 201

@app.route('/api/v1.0/getOffer', methods=['POST'])
def getOffer():
    if not request.json or not 'antrag_id' in request.json:
        abort(400)
    db = cls_dbAktionen()
    offer = db.getOffer(request.json['antrag_id'])
    if len(offer) == 0:
        abort(404)
    else:
        return jsonify({'offer': offer}), 201



if __name__ == '__main__':
    app.run(host='0.0.0.0', port='5005')