@komponentenintegrationstest
Feature: Speicherung eines neuen Kunden

  Scenario Outline: Speichern eines neuen Kunden, dessen Angaben bereits erfolgreich geprüft wurden
    Given Über die Schnittstelle kommt ein geprüfter Auftrag zur Kundenanlage
    When der Kunde hat die Rolle <rolle>
    When der Kunde hat die Anrede <anrede>
    When der Kunde hat den Vornamen <vorname>
    When der Kunde hat den Namen <name>
    When der Kunde wohnt in Strasse <strasse>
    When der Kunde wohnt in PLZ <plz>
    When der Kunde wohnt in Ort <ort>
    When der Kunde ist geboren am <geburtsdatum>
    Then der Kunde wurde erfolgreich in der Datenbank gespeichert

    Examples:
    | rolle | anrede  | vorname     | name      | strasse | plz    | ort      | geburtsdatum    |
    | 1     | 1       | Per-vorname | Per-name  | strasse | 12345  | ort      | 1973-11-17      |
    | 2     | 1       | Per-vorname | Per-name  | strasse | 12345  | ort      | 1973-11-17      |
    | 3     | 1       | Per-vorname | Per-name  | strasse | 12345  | ort      | 1973-11-17      |
    | 1     | 2       | Per-Horst   | Per-Müller| Plätze 1| 12345  | München  | heute - 18 y    |
    | 2     | 3       | Per-Horst   | Per-Müller| Plätze 1| 12345  | München  | gestern - 18 y  |