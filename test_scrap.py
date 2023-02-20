from selenium import webdriver
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.select import Select
from input_data import nie, nombre, age
from fake_useragent import UserAgent
import random



def scrab_web():

    while True:


        # user_agent variable
        useragent = UserAgent()

        #options
        options = webdriver.ChromeOptions()

        # user - agent
        options.add_argument(f"user-agent={useragent.random}")

        # disable webdriver mode
        options.add_argument("--disable-blink-features=AutomationControlled")

        # headless mode
        # options.add_argument("--headless")

        # options.add_argument('--disable-gpu')
        # options.add_argument('--remote-debugging-port=9222')
        # options.add_argument('--enable-javascript')
        # options.add_argument('--no-sandbox')
        # options.add_argument('--ignore-certificate-errors')
        # options.add_argument('--allow-insecure-localhost')

        # way to the cromewebdriver
        driver = webdriver.Chrome(executable_path="/home/shved15/my_pet_project/chromedriver", options=options)

        try:

            print("Going on website...")
            # going on website
            driver.get("https://icp.administracionelectronica.gob.es/icpplus/index.html")
            time.sleep(3)

            print("Choosing the city")
            # choosing the city
            choice1 = Select(driver.find_element(By.ID, "form"))
            choice1.select_by_visible_text("Tarragona")
            driver.implicitly_wait(5)

            print("Going on next webpage...")
            aceptar1 = driver.find_element(By.ID, "btnAceptar").click()
            time.sleep(3)

            print("Choosing the reason...")
            # driver.find_element(By.TAG_NAME, "body").send_keys(Keys.END)
            # time.sleep(2)

            # choosing the reason for petition
            choice2 = Select(driver.find_element(By.NAME,"tramiteGrupo[1]"))
            # choice2.select_by_visible_text("POLICIA- SOLICITUD ASILO")
            choice2.select_by_visible_text("POLICIA- EXPEDICIÓN/RENOVACIÓN DE DOCUMENTOS DE SOLICITANTES DE ASILO")
            driver.implicitly_wait(5)

            print("Going on next webpage...")
            aceptar2 = driver.find_element(By.ID, "btnAceptar").click()
            driver.implicitly_wait(5)

            print("Going on next webpage...")
            driver.find_element(By.TAG_NAME, "body").send_keys(Keys.END)
            driver.implicitly_wait(5)
            entrar = driver.find_element(By.ID, "btnEntrar").click()
            time.sleep(3)

            print("Adding the datas of person, and selecting country of citizenship...")
            # add prson data
            nie_input = driver.find_element(By.ID, "txtIdCitado")
            nie_input.clear()
            nie_input.send_keys(nie)
            time.sleep(1)

            nombre_input = driver.find_element(By.ID, "txtDesCitado")
            nombre_input.clear()
            nombre_input.send_keys(nombre)
            time.sleep(1)

            age_input = driver.find_element(By.ID, "txtAnnoCitado")
            age_input.clear()
            age_input.send_keys(age)
            time.sleep(1)

            choice3 = Select(driver.find_element(By.ID,"txtPaisNac"))
            choice3.select_by_visible_text("RUSIA")
            time.sleep(1)

            print("Going on next webpage...")
            aceptar3 = driver.find_element(By.ID, "btnEnviar").click()
            driver.implicitly_wait(5)

            print("Confirming the reservation...")
            solicitar_cita = driver.find_element(By.ID, "btnEnviar").click()
            time.sleep(5)

            result = ''
            try:
                check_seat = driver.find_element(By.CLASS_NAME, 'mf-input__xl')
                result += 'Yes'
            except Exception as ex:
                result += 'No'
        except Exception as ex:
            print(ex)
        finally:
            driver.close()
            driver.quit()

        if 'Yes' == result:
            break
        else:
            time.sleep(180)

    return result


        # time.sleep(180)

if __name__ == '__main__':
    scrab_web()
