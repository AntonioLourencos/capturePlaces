from datetime import date as Date, datetime as DateTime
from bs4 import BeautifulSoup as Bs
from selenium import webdriver as WebDriver

from modules.ScrollDown import scrollDown
from modules.Details import details
import pandas as pd

options = WebDriver.ChromeOptions()
options.add_argument("log-level=3")
options.add_argument("headless")

DRIVER = WebDriver.Chrome(chrome_options=options)


API_URL = "https://www.google.com/maps/search/"
JSAN_BOX = "7.Nv2PK,7.THOPZb,7.CpccDe,0.aria-label,0.role,0.jsaction"

QuerySearchPlace = "Shop Central Park, NY"


def FetchGoogleMaps(params: str):
    # print("[ SISTEMA ] - Iniciando Sistema...")

    # date = DateTime.now()
    # Sheet = f"{date.hour}-{date.minute}-{date.second}--{Date.today()}"

    # print("[ SISTEMA ] - Configurando...")
    # worksheet = pd.ExcelWriter(f"results/{Sheet}.xlsx", engine='xlsxwriter')

    # worksheet.close()

    DRIVER.get(API_URL + params.replace(" ", "+"))

    print("[ SISTEMA ] - Pronto!")
    print("[ SISTEMA ] - Iniciando Busca Por Resultados...")

    scrollDown(DRIVER)  # Scroll Down to get all places of table.

    print("[ SISTEMA ] - Finalizado Buscas")

    Content = Bs(DRIVER.page_source, "html.parser")

    Box = Content.findAll("div", jsan=JSAN_BOX)

    print("[ SISTEMA ] - Iniciando Captura De Dados")
    for box in Box:
        result = details(DRIVER, box)
        print(result)
        # worksheet.write_row(result)

    print("[ SISTEMA ] - ESCREVENDO DADOS")

    DRIVER.close()


if (__name__ == "__main__"):
    FetchGoogleMaps(QuerySearchPlace)
