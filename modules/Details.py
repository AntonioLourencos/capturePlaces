from bs4 import BeautifulSoup
from time import sleep

JSAN_DETAILS_BOX = "7.Io6YTe,7.fontBodyMedium"


def details(driver, box):
    detailsPageLink = box.find("a", jstcache="81").get("href")
    name = box.find("span", jstcache="128").text

    sleep(3)

    driver.get(detailsPageLink)

    detailsPage = BeautifulSoup(driver.page_source, "html.parser")
    detailsList = detailsPage.findAll("div", jsan=JSAN_DETAILS_BOX)

    address = ""
    phone = ""

    for index, value in enumerate(detailsList):

        if index == 0:
            address = value.text
        elif value.text.startswith("("):
            phone = value.text

    isRelavant = True if phone else False

    result = {
        "nome": name,
        "endereço": address,
        "telefone": phone,
        "isRelavant": isRelavant
    }

    return result
