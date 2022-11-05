@fixture.browser.chrome.headless @integration
Feature: Kunden erfassen

  Scenario Outline: Kunde erfassen Positivfälle
    Given Sachbearbeiter öffnet Webseite 'http://38.242.131.123:5000/addKunde'
    When Sachbearbeiter wählt <Rolle> in Feld *kundeRolle*
    When Sachbearbeiter wählt <Anrede> in Feld *kundeAnrede*
    When Sachbearbeiter schreibt <Name> in Feld *kundeName*
    When Sachbearbeiter schreibt <Vorname> in Feld *kundeVorname*
    When Sachbearbeiter schreibt <Strasse> in Feld *kundeStrasse*
    When Sachbearbeiter schreibt <Plz> in Feld *kundePlz*
    When Sachbearbeiter schreibt <Ort> in Feld *kundeOrt*
    When Sachbearbeiter schreibt <Geburtsdatum> in Feld *kundeGeburtsdatum*
    When Sachbearbeiter klickt auf Button [Kundendaten speichern]
    Then Das System antwortet mit Status <Status>

    Examples:
    | Rolle                   | Anrede        | Name            | Vorname       | Strasse         | Plz   | Ort         | Geburtsdatum  | Status                                      |
    | Juristische Person      | Frau          | Müller          | Marianne      | Hauptstrasse 2  | 20444 | Düsseldorf  | 24.12.1979    | Daten gespeichert für Kunde Marianne Müller |
    | Natürliche Person       | Herr          | Maier           | Hans          | Marktplatz 99   | 86654 | Obersdorf   | 01.01.1969    | Daten gespeichert für Kunde Hans Maier      |
    | Sonstiges               | Divers        | Huber           | Ditto         | Marienplatz 1   | 81369 | München     | 31.03.1984    | Daten gespeichert für Kunde Ditto Huber      |


  Scenario Outline: Kunde erfassen Negativfälle
    Given Sachbearbeiter öffnet Webseite 'http://38.242.131.123:5000/addKunde'
    When Sachbearbeiter wählt <Rolle> in Feld *kundeRolle*
    When Sachbearbeiter wählt <Anrede> in Feld *kundeAnrede*
    When Sachbearbeiter schreibt <Name> in Feld *kundeName*
    When Sachbearbeiter schreibt <Vorname> in Feld *kundeVorname*
    When Sachbearbeiter schreibt <Strasse> in Feld *kundeStrasse*
    When Sachbearbeiter schreibt <Plz> in Feld *kundePlz*
    When Sachbearbeiter schreibt <Ort> in Feld *kundeOrt*
    When Sachbearbeiter schreibt <Geburtsdatum> in Feld *kundeGeburtsdatum*
    When Sachbearbeiter klickt auf Button [Kundendaten speichern]
    Then Das System antwortet mit Returncode <Rc>

    Examples:
    | Rolle                   | Anrede        | Name            | Vorname       | Strasse         | Plz   | Ort         | Geburtsdatum  | Rc                                  |
    | Natürliche Person       | Herr          | Maier           | Horst         | Hauptstrasse 1  | xxxxx | München     | 17.11.1973    | PLZ nicht numerisch                 |
    | Natürliche Person       | Herr          | Ma              | Horst         | Hauptstrasse 1  | 12345 | München     | 17.11.1973    | Ungültiger Wert in Feld 'Name'      |
    | Natürliche Person       | Herr          | Maier           | Ho            | Hauptstrasse 1  | 12345 | München     | 17.11.1973    | Ungültiger Wert in Feld 'Vorname'   |
    | Natürliche Person       | Herr          | Maier           | Horst         | Ha              | 12345 | München     | 17.11.1973    | Ungültiger Wert in Feld 'Strasse'   |
    | Natürliche Person       | Herr          | Maier           | Horst         | Hauptstrasse 1  | 12345 | Mü          | 17.11.1973    | Ungültiger Wert in Feld 'Ort'       |

