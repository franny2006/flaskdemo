from behave import *
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support import expected_conditions as EC
from behave import fixture
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager



@given("Sachbearbeiter öffnet Webseite '{url}'")
def step_getUrl(context, url):
    context.driver.get(url)

@when("Sachbearbeiter wählt {selected} in Feld *{feldname}*")
def step_select(context, selected, feldname):
    feld = Select(context.driver.find_element(By.NAME, feldname))
    feld.select_by_visible_text(selected)

@when("Sachbearbeiter schreibt {inhalt} in Feld *{feldname}*")
def step_input(context, inhalt, feldname):
    el = WebDriverWait(context.driver, 20).until(EC.visibility_of_all_elements_located((By.NAME, feldname)))
    feld = context.driver.find_element(By.NAME, feldname)
    if feldname == "kundeGeburtsdatum" and context.browsertyp == "firefox":
        inhalt = inhalt[6:10] + "-" + inhalt[3:5] + "-" + inhalt[0:2]
        print(inhalt)
    feld.send_keys(inhalt)
    content = feld.get_attribute("value")
    print("Content nach SendKeys: ", content)
    if feldname != "kundeGeburtsdatum":
        assert content == inhalt, f'Der übergebene Wert {inhalt} konnte nicht ins Feld {feldname} eingetragen werden. Enthaltener Wert nach Erfassung: ' + content


@when("Sachbearbeiter klickt auf Button [{buttonname}]")
def step_click(context, buttonname):
    context.driver.find_element(By.XPATH, '//*[@value="' + buttonname + '"]').click()


@then("Das System antwortet mit Status {status}")
def step_result(context, status):
    statusKorrekt = False
    detail = ""

    try:
        statusSystem = context.driver.find_element(By.XPATH, "/html/body/ul/li[1]").text
        if status in statusSystem:
            statusKorrekt = True
            detail = "Erwarteter Status gefunden"
        else:
            statusKorrekt = False
            detail = "Tag gefunden, jedoch andere Rückmeldung (" + statusSystem + ")"
    except:
        statusSystem = None
        detail = "Tag nicht gefunden"

    assert statusKorrekt is True, f'Der erwartete Status = {status} wurde nicht gefunden. Detail: ' + detail



@then("Das System antwortet mit Returncode {returncode}")
def step_result(context, returncode):
    rcKorrekt = False

    try:
        rcSystem = context.driver.find_element(By.XPATH, "/html/body/ul/li[2]").text
        if returncode in rcSystem:
            rcKorrekt = True
        else:
            rcKorrekt = False
    except:
        rcSystem = None

    assert rcKorrekt is True, f'Returncode SOLL = {returncode} - IST = {rcSystem}'


@then("Die Übersichtsseite wird angezeigt")
def step_result(context):
    pass