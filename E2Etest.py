from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
import time
import random

# Imposta il driver di Chrome
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))

try:
    # Apri Google
    driver.get('https://www.google.com')

    # Aspetta qualche secondo per far caricare la pagina
    time.sleep(2)

    # Accetta i cookie (il selettore potrebbe dover essere aggiornato a seconda della lingua e dell'implementazione specifica della pagina)
    accept_cookies_button = driver.find_element(By.XPATH, '//*[@id="L2AGLb"]')
    accept_cookies_button.click()

    # Aspetta qualche secondo per permettere l'interazione con i cookie
    time.sleep(2)

    # Lista di termini di ricerca
    search_terms = ['selenium ide', 'python', 'https vs http', 'machine learning', 'java', 'machine learning']

    # Scegli un termine di ricerca casuale
    search_term = random.choice(search_terms)

    # Cerca il termine casuale nella barra di ricerca di Google
    search_box = driver.find_element(By.NAME, 'q')
    search_box.send_keys(search_term)
    search_box.send_keys(Keys.RETURN)

    # Aspetta che i risultati della ricerca vengano caricati
    time.sleep(2)

    # Clicca su "Immagini" per aprire Google Immagini
    images_link = driver.find_element(By.LINK_TEXT, 'Immagini')
    images_link.click()

    # Aspetta che le immagini vengano caricate
    time.sleep(2)

finally:
    # Chiudi il browser
    driver.quit()
