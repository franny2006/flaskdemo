from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
from selenium.webdriver.support.wait import WebDriverWait

driver = webdriver.Chrome('./chromedriver.exe')

driver.get("http://38.242.131.123:5000/addKunde")

WebDriverWait(driver, timeout=3).until(lambda d: d.find_element(By.NAME,"kundeRolle"))

rolle = Select(driver.find_element(By.NAME, "kundeRolle"))
rolle.select_by_visible_text('Natürliche Person')

anrede = Select(driver.find_element(By.NAME, "kundeAnrede"))
anrede.select_by_visible_text('Herr')

name = driver.find_element(By.NAME, "kundeName")
name.send_keys('Name...')

vorname = driver.find_element(By.NAME, "kundeVorname")
vorname.send_keys('Vorname...')

strasse = driver.find_element(By.NAME, "kundeStrasse")
strasse.send_keys('strasse...')

plz = driver.find_element(By.NAME, "kundePlz")
plz.send_keys('plz...')

ort = driver.find_element(By.NAME, "kundeOrt")
ort.send_keys('Ort...')

geburtsdatum = driver.find_element(By.NAME, "kundeGeburtsdatum")
geburtsdatum.send_keys('11.11.1977')

driver.find_element(By.XPATH, '//*[@value="Kundendaten speichern"]').click()


meldung = driver.find_element(By.XPATH, "/html/body/ul/li[2]").text
print("Response: ", meldung)