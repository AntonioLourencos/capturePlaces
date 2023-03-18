import xlsxwriter
from datetime import date as Date, datetime as DateTime
from bs4 import BeautifulSoup as Bs
from selenium import webdriver as WebDriver

from ScrollDown import scrollDown
from Details import details

options = WebDriver.ChromeOptions()
options.add_argument("log-level=3")
# Closed
options.add_argument("headless")

# Opened
# options.add_experimental_option("detach", True)

DRIVER = WebDriver.Chrome(chrome_options=options)


API_URL = "https://www.google.com/maps/search/"
JSAN_BOX = "7.Nv2PK,7.THOPZb,7.CpccDe,0.aria-label,0.role,0.jsaction"

QuerySearchPlace = "loja, Samambaia Sul, Brasília - DF"


def FetchGoogleMaps(params):
    print("[ SISTEMA ] - Iniciando Sistema...")

    date = DateTime.now()
    Sheet = f"{date.hour}-{date.minute}-{date.second}--{Date.today()}"

    print("[ SISTEMA ] - Configurando...")

    workbook = xlsxwriter.Workbook(f'results/{Sheet}.xlsx')
    worksheet = workbook.add_worksheet()

    headers = ["Nome", "Endereço", "Telefone", "É relevante"]
    worksheet.write_row(0, 0, headers)

    try:
        DRIVER.get(API_URL + params.replace(" ", "+"))

        print("[ SISTEMA ] - Pronto!")
        print("[ SISTEMA ] - Iniciando Busca Por Resultados...")

        scrollDown(DRIVER)  # Scroll Down to get all places of table.

        print("[ SISTEMA ] - Finalizado Buscas")

        Content = Bs(DRIVER.page_source, "html.parser")

        Box = Content.findAll("div", role="article")

        print("[ SISTEMA ] - Iniciando Captura De Dados e Inserção de dados.")

        for rowNumber, box in enumerate(Box):
            result = details(DRIVER, box)
            worksheet.write_row(rowNumber + 1, 0, result)

        print("[ SISTEMA ] - Dados Escritos!")
    except:
        print("[ SISTEMA ] - Aconteceu um erro e o sistema não pode continuar a captura e inserção de dados.")

    DRIVER.close()
    workbook.close()
    print("[ SISTEMA ] - FINALIZADO! ")


if (__name__ == "__main__"):
    FetchGoogleMaps(QuerySearchPlace)
