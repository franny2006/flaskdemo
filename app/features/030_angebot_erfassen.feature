@fixture.browser.chrome.ui @systemtest @systemintegrationstest
Feature: Angebote erfassen

  Scenario Outline: Angebot erfassen Positivfälle
    Given Sachbearbeiter öffnet Webseite 'http://38.242.131.123:5000/addOffer'
    When Sachbearbeiter schreibt <Antragsteller> in Feld *angebotKundeNameAuswahl*
    When Sachbearbeiter schreibt <Geburtsdatum> in Feld *angebotKundeGeburtsdatum*
    When Sachbearbeiter schreibt <Führerscheindatum> in Feld *angebotFuehrerschein*
    When Sachbearbeiter schreibt <Hersteller> in Feld *angebotHersteller*
    When Sachbearbeiter schreibt <HSN> in Feld *angebotHsn*
    When Sachbearbeiter schreibt <Typ> in Feld *angebotTyp*
    When Sachbearbeiter schreibt <TSN> in Feld *angebotTsn*
    When Sachbearbeiter schreibt <Kategorie> in Feld *angebotKategorie*
    When Sachbearbeiter schreibt <EZ> in Feld *angebotErstzulassung*
    When Sachbearbeiter wählt <KM> in Feld *angebotKilometer*
    When Sachbearbeiter wählt <Verwendung> in Feld *angebotVerwendung*
    When Sachbearbeiter schreibt <Beginn> in Feld *angebotVersicherungsbeginn*
    When Sachbearbeiter klickt auf Button [Antrag speichern]
    Then Die Übersichtsseite wird angezeigt

    Examples:
    | Antragsteller         | Geburtsdatum | Führerscheindatum | Hersteller            | HSN   | Typ         | TSN   | Kategorie         | EZ          | KM        | Verwendung | Beginn     |
    | Mustermann, Maria     | 17.11.1968   | 22.10.1988        | BAYER.MOT.WERKE-BMW   | 005   | 330D        | 661   | Limousine         | 01.10.2022  | 20.000    | privat     | 01.11.2022 |
    | Mustermann, Maria     | 17.11.1968   | 22.10.1988        | Audi                  | 0588  | A4          | 748   | Kombi             | 01.10.2022  | 20.000    | privat     | 01.11.2022 |
    | Mustermann, Maria     | 17.11.1968   | 22.10.1988        | Mercedes              | 2222  | AMG-GT      | AAO   | Cabrio            | 01.10.2022  | 20.000    | privat     | 01.11.2022 |



