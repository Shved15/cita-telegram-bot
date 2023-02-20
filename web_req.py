import requests
import time
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.select import Select
from fake_useragent import UserAgent
from multiprocessing import Pool
import random
from data_web_for_bot import names_of_provinces




def get_data_page_2(url):
    # for province in names_of_provinces['Tarragona']:
    useragent = UserAgent()

    options = webdriver.ChromeOptions()
    options.add_argument(f"user-agent={useragent.random}")
    options.add_argument("--disable-blink-features-AutomationControlled")

    # for province in names_of_provinces[:1]:

    try:

        driver = webdriver.Chrome(executable_path="/home/shved15/my_pet_project/chromedriver", options=options)
        driver.get(url=url)
        time.sleep(3)

        choice_prov = Select(driver.find_element(By.ID, "form"))
        choice_prov.select_by_visible_text('Tarragona')
        driver.implicitly_wait(5)

        print("Going on next webpage...")
        aceptar1 = driver.find_element(By.ID, "btnAceptar").click()
        time.sleep(5)

        # with open("pages_requests/pages_Barcelona/index_Barcelona.html", "w") as file:
        #     file.write(driver.page_source)

        choice2 = Select(driver.find_element(By.NAME,"tramiteGrupo[1]"))
        # choice2.select_by_visible_text("POLICIA- SOLICITUD ASILO")
        choice2.select_by_visible_text("POLICIA- EXPEDICIÓN/RENOVACIÓN DE DOCUMENTOS DE SOLICITANTES DE ASILO")
        # driver.implicitly_wait(5)
        time.sleep(3)

        print("Going on next webpage...")
        aceptar2 = driver.find_element(By.ID, "btnAceptar").click()
        driver.implicitly_wait(5)
        # time.sleep(5)

        print("Going on next webpage...")
        driver.find_element(By.TAG_NAME, "body").send_keys(Keys.END)
        driver.implicitly_wait(5)
        entrar = driver.find_element(By.ID, "btnEntrar").click()
        time.sleep(3)

        print("Adding the datas of person, and selecting country of citizenship...")
        # add prson data
        nie_input = driver.find_element(By.ID, "txtIdCitado")
        nie_input.clear()
        nie_input.send_keys('z0265169f')
        time.sleep(1)

        nombre_input = driver.find_element(By.ID, "txtDesCitado")
        nombre_input.clear()
        nombre_input.send_keys('maxim maximov')
        time.sleep(1)

        age_input = driver.find_element(By.ID, "txtAnnoCitado")
        age_input.clear()
        age_input.send_keys('1998')
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

        try:
            check_seat = driver.find_element(By.CLASS_NAME, 'mf-input__xl')
            print("С этого моменты начинается активация бота\nон отправляет увдомление о наличии свободных мест")
        except Exception as ex:
            print("fuuuuckkk")

        # with open("/home/shved15/my_pet_project/provinces_INFO/pages_Tarragona/index_Tarragona_3.html", "w") as file:
        #     file.write(driver.page_source)


    except Exception as ex:
        print(ex)
    finally:
        driver.close()
        driver.quit()



def main():
    get_data_page_2("https://icp.administracionelectronica.gob.es/icpplus/index.html")


if __name__ == '__main__':
    main()
#     process_count = 2
#     url = "https://icp.administracionelectronica.gob.es/icpplus/index.html"
#     urls_list = [url] * process_count
#     p=Pool(processes=process_count)
#     p.map(get_data_page_2, urls_list)
