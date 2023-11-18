*** Settings ***
Library  SeleniumLibrary
Library  ../AppLibrary.py
Library  OperatingSystem

*** Variables ***
${SERVER}  localhost:5001
${DELAY}  0.0 seconds
${HOME_URL}  http://${SERVER}
${LOGIN_URL}  http://${SERVER}/login
${REGISTER_URL}  http://${SERVER}/register

*** Keywords ***
Open And Configure Browser

    # Asetettava geckodriverin bugin takia. Todellisessa ympäristössä toinen workaround
    Set Environment Variable  name=TMPDIR  value=/home/otso/tmp

    # jos käytät Firefoxia ja Geckodriveriä käytä seuraavaa riviä sitä alemman sijaan
    ${options}  Evaluate  sys.modules['selenium.webdriver'].FirefoxOptions()  sys
    # ${options}  Evaluate  sys.modules['selenium.webdriver'].ChromeOptions()  sys
    Call Method    ${options}    add_argument    --no-sandbox
    # seuraava rivi on kommentoitu toistaiseksi pois
    Call Method  ${options}  add_argument  --headless
    Open Browser  browser=firefox  options=${options}
    Set Selenium Speed  ${DELAY}

Login Page Should Be Open
    Title Should Be  Login

Main Page Should Be Open
    Title Should Be  Ohtu Application main page

Register Page Should Be Open
    Title Should Be  Register

Go To Login Page
    Go To  ${LOGIN_URL}

Go To Starting Page
    Go To  ${HOME_URL}

Go To Register Page
    Go To  ${REGISTER_URL}