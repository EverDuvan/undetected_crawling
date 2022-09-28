from concurrent.futures import ThreadPoolExecutor, thread
from selenium.webdriver.common.by import By
import psycopg2
from selenium import webdriver
import undetected_chromedriver as uc
from selenium import webdriver
from ProductDetailModel import ProductDetailModel
from Proxys import proxyRandom
import SamsClub
from testSaveBD import guardarDB
import time


class Datasheet:

    def __init__(self, id, country, retail, countryRetail, category, subcategory, urlCategory, webName):
        self.id = id
        self.country = country
        self.retail = retail
        self.countryRetail = countryRetail
        self.category = category
        self.subcategory = subcategory
        self.urlCategory = urlCategory
        self.webName = webName


conexion = psycopg2.connect(
    host="209.145.53.141", database="narbiTaIdA", user="sant", password="w7*yW7&bAasK")
cur = conexion.cursor()
cur.execute("SELECT \"id\",\"country\",\"retail\",\"countryRetail\",\"category\",\"subcategory\",\"urlCategory\",\"webName\" " +
            "FROM retail_information WHERE \"country\" IN ('USA') and \"retail\" in (E'SAM\\'S CLUB')")


crawling = []

for id, country, retail, countryRetail, category, subcategory, urlCategory, webName in cur.fetchall():
    craw = Datasheet(id, country, retail, countryRetail,
                     category, subcategory, urlCategory, webName)
    crawling.append(craw)

conexion.close()


def getUrls(driver):

    urlsList = []

    try:
        if len(driver.find_elements(By.CSS_SELECTOR, 'div.sc-pc-medium-desktop-card > a')) > 0:
            url = driver.find_elements(
                By.CSS_SELECTOR, 'div.sc-pc-medium-desktop-card > a')
        for i in url:
            urlsList.append(i.get_attribute('href'))
    except:
        print('Error')
    return urlsList


def startScrapProducts(urls, craw):

    try:

        for url in urls:

            chrome_options = webdriver.ChromeOptions()
            chrome_options.add_argument('--proxy-server=' + str(proxyRandom()))
            chrome_options.add_argument('--headless')
            driver = uc.Chrome(options=chrome_options)
            driver.get(url)
            time.sleep(3)

            if driver.page_source != None:
                name = SamsClub.getName(driver)
                if name != None:
                    price = SamsClub.getPrice(driver)
                    image = SamsClub.getImage(driver)
                    description = SamsClub.getDescription(driver)
                    model = SamsClub.getModel(driver)
                    brand = SamsClub.getBrand(driver)
                    sku = SamsClub.getSku(driver)

            producto = ProductDetailModel(craw.retail,
                                          name,
                                          url,
                                          brand,
                                          model,
                                          description,
                                          price,
                                          image,
                                          craw.country,
                                          craw.category,
                                          craw.subcategory,
                                          ' hola ',
                                          sku,
                                          craw.webName,
                                          ' hola ')
            print(producto.price)

            guardarDB(producto)
            driver.quit()

    except:
        print('Error StartScraperProducts')


def startAll(craw):

    chrome_options = webdriver.ChromeOptions()
    chrome_options.add_argument('--proxy-server=' + str(proxyRandom()))
    chrome_options.add_argument('--headless')
    driver = uc.Chrome(options=chrome_options)
    driver.get(craw.urlCategory)
    time.sleep(5)
    urls = getUrls(driver)
    driver.quit()
    startScrapProducts(urls, craw)


if __name__ == '__main__':

    executor = ThreadPoolExecutor(max_workers=2)

    for craw in crawling:
        executor.submit(startAll, craw)
