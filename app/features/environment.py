from behave import *
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.chrome.options import Options
from behave import fixture
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

def before_tag(context, tag):
    if tag == "fixture.browser.chrome.headless":
        open_browser(context, "chrome", "aktiv")
    elif tag == "fixture.browser.chrome.ui":
        open_browser(context, "chrome", "inaktiv")
    elif tag == "fixture.browser.firefox.ui":
        open_browser(context, "firefox", "inaktiv")
    elif tag == "fixture.browser.firefox.headless":
        open_browser(context, "firefox", "aktiv")



def open_browser(context, browsertyp, status_headless):
    # -- SETUP-FIXTURE PART: And register as context-cleanup task.


    if browsertyp == "chrome":
        options = Options()
    #    options.binary_location = "/usr/local/bin/chromedriver"
        options.add_argument('--no-sandbox')
        options.add_argument('--window-size=2560,1440')
        if status_headless == 'aktiv':
            options.headless = True
        else:
            options.headless = False
        # browser = webdriver.Chrome('./features/steps/webdriver/chromedriver.exe', options=options)
        browser = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)
      #  browser = webdriver.Chrome('/usr/local/bin/chromedriver', options=options)

        context.browsertyp = "chrome"
    else:
        options = webdriver.FirefoxOptions()
        if status_headless == 'aktiv':
            options.add_argument("--headless")
        browser = webdriver.Firefox('./features/steps/webdriver/', options=options)
        # browser = webdriver.Firefox('', options=options)
        context.browsertyp = "firefox"


    context.driver = browser
    return browser