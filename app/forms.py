from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, BooleanField, SelectField, SubmitField, HiddenField, SelectMultipleField
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
    kundeId = HiddenField('KundeId')
    kundeRolle = SelectField('Rolle', choices=[('', 'Bitte auswählen'), ('1', 'Natürliche Person'), ('2', 'Juristische Person'), ('3', 'Sonstiges')], validators=[DataRequired(message="Pflichtfeld")])
    kundeAnrede = SelectField('Anrede', choices=[('', 'Bitte auswählen'), ('1', 'Herr'), ('2', 'Frau'), ('3', 'Divers')], validators=[DataRequired(message="Pflichtfeld")])
    kundeName = StringField('Name', validators=[DataRequired(message="Pflichtfeld")])
    kundeVorname = StringField('Vorname', validators=[DataRequired(message="Pflichtfeld")])
    kundeStrasse = StringField('Straße', validators=[DataRequired(message="Pflichtfeld")])
    kundePlz = StringField('PLZ', validators=[DataRequired(message="Pflichtfeld")])
    kundeOrt = StringField('Ort', validators=[DataRequired(message="Pflichtfeld")])
    submit = SubmitField('Kundendaten speichern')


class TarifForm(FlaskForm):
    tarifId = HiddenField('TarifId')
    tarifName = StringField('Titel', validators=[DataRequired(message="Pflichtfeld")])
    tarifBausteine = SelectMultipleField('Bausteine', choices=[('1', 'freie Werkstattwahl'), ('2', 'Restwertversicherung')])
    tarifWert = StringField('Basiswert', validators=[DataRequired(message="Pflichtfeld")])
    tarifVst = StringField('Höhe VSt', validators=[DataRequired(message="Pflichtfeld")])
    submit = SubmitField('Tarif speichern')

class AngebotForm_1(FlaskForm):
    angebotId = HiddenField('angebotId')
    angebotKundeId = HiddenField('KundenID', validators=[DataRequired(message="Pflichtfeld")])
    angebotKundeName = StringField('Name des Antragstellers', validators=[DataRequired(message="Pflichtfeld")])
    angebotKundeVorname = StringField('')
    angebotKundeName2 = StringField('')
    angebotKundeStrasse = StringField('')
    angebotKundePlz = StringField('')
    angebotKundeOrt = StringField('')
    angebotPartnerId = HiddenField('PartnerID', validators=[DataRequired(message="Pflichtfeld")])
    angebotPartnerName = StringField('Name des Vermittlers', validators=[DataRequired(message="Pflichtfeld")])
    angebotPartnerVorname = StringField('')
    angebotPartnerName2 = StringField('')
    angebotPartnerStrasse = StringField('')
    angebotPartnerPlz = StringField('')
    angebotPartnerOrt = StringField('')
    angebotTarifId = HiddenField('TarifId', validators=[])
    angebotTarifName = StringField('gewünschter Tarif', validators=[])
    submit = SubmitField('Antrag speichern')

class AngebotForm_2(FlaskForm):
    angebotTarifName2 = SelectField('Tarif', choices=[], coerce=int)
    submit = SubmitField('Antrag speichern')