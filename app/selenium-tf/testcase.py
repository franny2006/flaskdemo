from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
from selenium.webdriver.support.wait import WebDriverWait
import time

driver = webdriver.Chrome('./chromedriver.exe')

driver.get("http://38.242.131.123:5000/addOffer")

WebDriverWait(driver, timeout=3).until(lambda d: d.find_element(By.NAME,"angebotKundeNameAuswahl"))

name = driver.find_element(By.NAME, "angebotKundeNameAuswahl")
name.send_keys('Müller, Marianne')

name = driver.find_element(By.NAME, "angebotKundeGeburtsdatum")
name.send_keys('17.11.1968')

name = driver.find_element(By.NAME, "angebotFuehrerschein")
name.send_keys('17.11.1988')

name = driver.find_element(By.NAME, "angebotHersteller")
name.send_keys('BMW')
time.sleep(1)

name = driver.find_element(By.NAME, "angebotHsn")
name.send_keys('005')

name = driver.find_element(By.NAME, "angebotTyp")
name.send_keys('330D, 661, (Anz. Zulassungen: 1.152)')

name = driver.find_element(By.NAME, "angebotTsn")
name.send_keys('661')

name = driver.find_element(By.NAME, "angebotKategorie")
name.send_keys('Limousine')

name = driver.find_element(By.NAME, "angebotErstzulassung")
name.send_keys('17.11.2021')

rolle = Select(driver.find_element(By.NAME, "angebotKilometer"))
rolle.select_by_visible_text('20.000')

rolle = Select(driver.find_element(By.NAME, "angebotVerwendung"))
rolle.select_by_visible_text('privat')

name = driver.find_element(By.NAME, "angebotVersicherungsbeginn")
name.send_keys('01.11.2022')




driver.find_element(By.XPATH, '//*[@value="Antrag speichern"]').click()


#meldung = driver.find_element(By.XPATH, "/html/body/ul/li[2]").text
#print("Response: ", meldung)