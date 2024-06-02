import os
import time
import random
import pyautogui
from PIL import ImageGrab
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys


def check_for_updates():
    # Apri il menu delle applicazioni
    pyautogui.hotkey('alt', 'f1')
    time.sleep(1)

    # Digita "Impostazioni"
    pyautogui.write('Impostazioni')
    time.sleep(1)

    # Premi "Invio" per aprire le impostazioni
    pyautogui.press('enter')
    time.sleep(3)  # Attendi che le impostazioni si aprano

    # Naviga al menu "Aggiornamenti"
    pyautogui.write('Aggiornamenti')
    time.sleep(1)
    pyautogui.press('enter')
    time.sleep(3)  # Attendi che il menu si apra

    # Fai clic sul primo risultato
    pyautogui.click(969, 210)
    time.sleep(5)  # Attendi la verifica degli aggiornamenti

    # Fai clic sul secondo risultato
    pyautogui.click(1509, 172)
    time.sleep(5)  # Attendi la verifica degli aggiornamenti

    # Mantieni aperta la finestra per permettere l'installazione degli aggiornamenti
    time.sleep(60)  # Attendi un minuto per consentire l'installazione

    # Chiudi la finestra delle impostazioni
    pyautogui.hotkey('alt', 'f4')


# Configurazione del driver Selenium
chrome_options = webdriver.ChromeOptions()
chrome_options.add_argument("--start-maximized")
chrome_options.add_argument("--disable-notifications")
driver = webdriver.Chrome(options=chrome_options)

# Apre il browser
driver.get("https://www.google.com/")
check_for_updates()

# Accetta i cookie
driver.find_element(By.ID, "L2AGLb").click()

# Liste di parole chiave per la ricerca casuale
keywords = ["openai", "machine learning", "artificial intelligence", "python programming", "data science"]

# Selezione casuale di una parola chiave
random_keyword = random.choice(keywords)

# Cerca la parola chiave su Google
search_box = driver.find_element(By.NAME, "q")
search_box.send_keys(random_keyword)
search_box.send_keys(Keys.RETURN)

# Attendi un po' per caricare i risultati
time.sleep(2)

# Apre il primo link dei risultati
first_link = driver.find_element(By.CSS_SELECTOR, ".tF2Cxc:nth-of-type(1) a")
first_link.click()

# Attendi un po' per caricare il sito
time.sleep(2)

# Torna alla pagina precedente
driver.back()

# Chiudi il browser
driver.quit()

# Calcola la risoluzione e la frequenza di aggiornamento dello schermo
width, height, frequency = get_screen_info()
print(f"Risoluzione dello schermo: {width}x{height}")
print(f"Frequenza di aggiornamento: {frequency} Hz")

# Attendi un po'
time.sleep(2)

# Configurazione del driver Selenium per il test di velocità
driver = webdriver.Chrome(options=chrome_options)

# Apre il browser
driver.get("https://www.google.com/")

# Accetta i cookie se necessario
try:
    driver.find_element(By.ID, "L2AGLb").click()
except:
    pass

# Cerca "Ookla Speed Test" su Google
search_box = driver.find_element(By.NAME, "q")
search_box.send_keys("Ookla Speed Test")
search_box.send_keys(Keys.RETURN)

# Attendi un po' per caricare i risultati
time.sleep(2)

# Clicca sul primo link dei risultati (di solito il link diretto a Ookla)
first_link = driver.find_element(By.CSS_SELECTOR, ".tF2Cxc:nth-of-type(1) a")
first_link.click()

# Attendi che la pagina di Ookla si carichi completamente
time.sleep(5)

# Tenta di cliccare il bottone di inizio test di velocità
try:
    start_button = driver.find_element(By.ID, "onetrust-accept-btn-handler")
    start_button.click()  # Clicca su accetta cookie se compare
except NoSuchElementException:
    pass

try:
    go_button = driver.find_element(By.CLASS_NAME, "start-text")
    go_button.click()
except NoSuchElementException:
    print("Il bottone per iniziare il test di velocità non è stato trovato.")

# Attendi durante il test di velocità
print("Test di velocità in corso...")

time.sleep(50)  # Tempo stimato per completare il test

# Esegui uno screenshot della pagina corrente
screenshot_path = "pagina_precedente.png"
driver.save_screenshot(screenshot_path)

# Chiudi il browser
driver.quit()
print("Browser chiuso dopo 10 secondi.")
