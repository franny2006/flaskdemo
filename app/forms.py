from flask_wtf import FlaskForm
from wtforms import StringField, SelectField, SubmitField, HiddenField, SelectMultipleField, DateField

from wtforms.validators import DataRequired

class PartnerForm(FlaskForm):
    partnerId = HiddenField('PartnerId')
    partnerRolle = SelectField('Rolle', choices=[('', 'Bitte auswählen'), ('1', 'Vermittler'), ('2', 'Agentur'), ('3', 'Sonstiges')], validators=[DataRequired(message="Pflichtfeld")])
    partnerAnrede = SelectField('Anrede', choices=[('', 'Bitte auswählen'), ('1', 'Herr'), ('2', 'Frau'), ('3', 'Firma')], validators=[DataRequired(message="Pflichtfeld")])
    partnerName = StringField('Name', validators=[DataRequired(message="Pflichtfeld")])
    partnerVorname = StringField('Vorname', validators=[DataRequired(message="Pflichtfeld")])
    partnerStrasse = StringField('Straße', validators=[DataRequired(message="Pflichtfeld")])
    partnerPlz = StringField('PLZ', validators=[DataRequired(message="Pflichtfeld")])
    partnerOrt = StringField('Ort', validators=[DataRequired(message="Pflichtfeld")])
    submit = SubmitField('Partnerdaten speichern')


class KundeForm(FlaskForm):
    kunde_id = HiddenField('kunde_id')
    kundeRolle = SelectField('Rolle', choices=[('', 'Bitte auswählen'), ('1', 'Natürliche Person'), ('2', 'Juristische Person'), ('3', 'Sonstiges')], validators=[DataRequired(message="Pflichtfeld")])
    kundeAnrede = SelectField('Anrede', choices=[('', 'Bitte auswählen'), ('1', 'Herr'), ('2', 'Frau'), ('3', 'Divers')], validators=[DataRequired(message="Pflichtfeld")])
    kundeName = StringField('Name', validators=[DataRequired(message="Pflichtfeld")])
    kundeVorname = StringField('Vorname', validators=[DataRequired(message="Pflichtfeld")])
    kundeStrasse = StringField('Straße', validators=[DataRequired(message="Pflichtfeld")])
    kundePlz = StringField('PLZ', validators=[DataRequired(message="Pflichtfeld")])
    kundeOrt = StringField('Ort', validators=[DataRequired(message="Pflichtfeld")])
    kundeGeburtsdatum = DateField('Geburtsdatum', format='%Y-%m-%d')
    submit = SubmitField('Kundendaten speichern')


class TarifForm(FlaskForm):
    tarifId = HiddenField('TarifId')
    tarifName = StringField('Titel', validators=[DataRequired(message="Pflichtfeld")])
    tarifBausteine = SelectMultipleField('Bausteine', choices=[('1', 'freie Werkstattwahl'), ('2', 'Restwertversicherung')])
    tarifWert = StringField('Basiswert', validators=[DataRequired(message="Pflichtfeld")])
    tarifVst = StringField('Höhe VSt', validators=[DataRequired(message="Pflichtfeld")])
    submit = SubmitField('Tarif speichern')

class OfferForm(FlaskForm):
    angebotId = HiddenField('angebotId')
    angebotKundeId = HiddenField()
    angebotKundeNameAuswahl = StringField('Antragsteller', validators=[DataRequired(message="Pflichtfeld")])
    angebotKundeName = StringField('Angaben zum Antragsteller', validators=[DataRequired(message="Pflichtfeld")])
    angebotKundeVorname = StringField('Vorname')
    angebotKundeStrasse = StringField('Straße')
    angebotKundePlz = StringField('PLZ')
    angebotKundeOrt = StringField('Ort')
    angebotFuehrerschein = DateField('Führerschein seit', format='%Y-%m-%d')
    angebotKundeGeburtsdatum = DateField('Geburtsdatum', format='%Y-%m-%d')
    angebotHersteller = StringField('Hersteller')
    angebotTyp = StringField('Fahrzeugtyp')
    angebotHsn = StringField('HSN')
    angebotTsn = StringField('TSN')
    angebotErstzulassung = DateField('Erstzulassung', format='%Y-%m-%d')
    angebotTarifId = HiddenField('TarifId', validators=[])
    angebotTarifName = StringField('gewünschter Tarif', validators=[])
    angebotKategorie = SelectField('Fahrzeugkategorie', choices=[('*** Bitte auswählen ***'), ('Limousine'), ('Kombi'), ('Cabrio')])
    angebotVerwendung = SelectField('Verwendung', choices=[('*** Bitte auswählen ***'), ('privat'), ('gewerblich'), ('privat und gewerblich')])
    angebotKilometer = SelectField('jährliche Fahrleistung', choices=[('*** Bitte auswählen ***'), ('10.000'), ('20.000'), ('30.000'), ('50.000')])
    angebotVersicherungsbeginn = DateField('gewünschter Versicherungsbeginn', format='%Y-%m-%d')
    submit = SubmitField('Antrag speichern')

class AngebotForm_2(FlaskForm):
    angebotTarifName2 = SelectField('Tarif', choices=[], coerce=int)
    submit = SubmitField('Antrag speichern')