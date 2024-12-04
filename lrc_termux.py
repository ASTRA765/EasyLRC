"""LRC Downloader"""
import sys
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.firefox.service import Service
from selenium.webdriver.firefox.options import Options
import time

#Variables iniciales
url_base = "https://lrclib.net/search/"
url_edit = url_base + "%20".join(sys.argv[1:])
name = "_".join(sys.argv[1:])

options = Options()
options.headless = True

service = Service("/data/data/com.termux/files/usr/bin/geckodriver")

driver = webdriver.Firefox(service=service, options=options)

#Funciones
def acceso_web():
    try:
        driver.get(url_edit)
        time.sleep(3)
        clic_boton = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.CSS_SELECTOR, ".rounded.text-indigo-700"))
        )
        clic_boton.click()
        time.sleep(2)
        obtener_letra = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.CSS_SELECTOR, ".grow.rounded.bg-indigo-50.text-indigo-900.whitespace-pre-line.p-4.overflow-scroll"))
        )
        letra_texto = obtener_letra.text
        print(letra_texto)
        return letra_texto
    except Exception as e:
        print("Error en la request:"+ str(e))
        return None, None
    finally:
        driver.quit()

#Ejecucion
letra_texto = acceso_web()
if letra_texto:
    file_name = name+".lrc"
    with open(file_name, "w", encoding="utf-8") as file:
        file.write(letra_texto)
        print("Letras guardadas en:" + file_name)