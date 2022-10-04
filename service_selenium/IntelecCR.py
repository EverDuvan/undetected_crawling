from asyncio import exceptions
from selenium.webdriver.common.by import By
from model.Product import ProductDetailModel
import undetected_chromedriver as uc
from controller.DBController import guardarDB
from controller.SeleniumController import start_driver, open_url
from concurrent.futures import ThreadPoolExecutor

def start_crawling(datasheet):

    driver = start_driver()
    urls = getUrls(driver, datasheet.urlCategory)
    driver.quit()

    for url in urls:
        startScrapProducts(url,datasheet)
        

def getUrls(driver, url):

    urlsList = []

    try:
        open_url(url,driver)
        
        if len(driver.find_elements(By.CSS_SELECTOR, 'div.product-thumb.transition>div.image>a')) > 0:
            url = driver.find_elements(By.CSS_SELECTOR, 'div.product-thumb.transition>div.image>a')
        for i in url:
            urlsList.append(i.get_attribute('href'))
    except Exception as e:
        print(e)
    return urlsList


def startScrapProducts(url, datasheet):

    try:

        driver = start_driver()
        open_url(url,driver)

        if driver.page_source != None:
            name = getName(driver)
            if name != None:
                price = getPrice(driver)
                image = getImage(driver)
                description = getDescription(driver)
                model = getModel(driver)
                brand = getBrand(driver)
                sku = getSku(driver)

        print(name)

        producto = ProductDetailModel(datasheet.retail, name, url, brand, model, description,
                                      price, image, datasheet.country, datasheet.category, datasheet.subcategory, '', sku, datasheet.webName, '')
        

        #guardarDB(producto)
        driver.quit()

    except:
        print('Error StartScraperProducts')




# ------------------------ NAME ---------------------------------------------------


def getName(driver):
    """
    If there is an element with the tag h1, then get the text of that element and assign it to the
    variable name

    :param driver: the webdriver object
    :return: The name of the person
    """
    name = ''
    try:
        if len(driver.find_elements(By.XPATH, '//h1')) > 0:
            name = driver.find_element(By.XPATH, '//h1').text
    except:
        print('Error traer name')
    return (name)

# ------------------------ PRICE---------------------------------------------------


def getPrice(driver):
    """
    It tries to find the price of the product on the page, and if it can't find it, it returns an empty
    string

    :param driver: the webdriver object
    :return: The price of the product
    """
    price = ''
    try:
        if len(driver.find_elements(By.XPATH, '//meta[contains(@itemprop, \"price\")]')) > 0:
            price = driver.find_element(
                By.XPATH, '//meta[contains(@itemprop, \"price\")]').get_attribute('content')
    except:
        print('Error traer price')
    return (price)

# ------------------------ DESCRIPTION ---------------------------------------------------


def getDescription(driver):
    """
    If there are any elements with the CSS selector 'div.sc-description-about-long' then get the text of
    each of those elements and join them together with a comma

    :param driver: the webdriver object
    :return: A list of strings.
    """
    list = []
    desc = ''
    try:
        if len(driver.find_elements(By.CSS_SELECTOR, 'div.sc-description-about-long')) > 0:
            elemntos = []
            elemntos = driver.find_elements(
                By.CSS_SELECTOR, 'div.sc-description-about-long > p')
            for elemento in elemntos:
                list.append(elemento.text)
            desc = ', '.join(list)
    except:
        print('Error traer price')
    return desc

# ------------------------ SKU ---------------------------------------------------


def getSku(driver):
    """
    If there are any elements that match the XPATH, then get the content of the first one.

    :param driver: the webdriver object
    :return: A list of dictionaries.
    """
    sku = ''
    try:
        if len(driver.find_elements(By.XPATH, '//meta[contains(@itemprop, \"sku\")]')) > 0:
            sku = driver.find_element(
                By.XPATH, '//meta[contains(@itemprop, \"sku\")]').get_attribute('content')
    except:
        print('Error traer sku')
    return (sku)

# ------------------------ BRAND ---------------------------------------------------


def getBrand(driver):
    """
    If there is a span element with the class sc-product-header-item-number, then get the text of that
    element and return it

    :param driver: the webdriver object
    :return: The brand of the product
    """
    brand = ''
    try:
        if len(driver.find_elements(By.CSS_SELECTOR, 'span.sc-product-header-item-number')) > 0:
            brand = driver.find_element(
                By.CSS_SELECTOR, 'span.sc-product-header-item-number').text
            if "By" in brand:
                brand = brand.replace("By", "").strip()
    except:
        print('Error traer sku')
    return brand

# ------------------------ MODEL ---------------------------------------------------


def getModel(driver):
    model = ''
    try:
        if len(driver.find_elements(By.XPATH, '//meta[contains(@itemprop, \"mpn\")]')) > 0:
            model = driver.find_element(
                By.XPATH, '//meta[contains(@itemprop, \"mpn\")]').get_attribute('content')
    except:
        print('Error traer sku')
    return model

# ------------------------ IMAGE ---------------------------------------------------


def getImage(driver):
    """
    If there is an element with an xpath that contains the string "og:image" in the attribute
    "property", then get the content of that element

    :param driver: the webdriver object
    :return: The image url
    """
    image = ''
    try:
        if len(driver.find_elements(By.XPATH, '//meta[contains(@property, \"og:image\")]')) > 0:
            image = driver.find_element(
                By.XPATH, '//meta[contains(@property, \"og:image\")]').get_attribute('content')
    except:
        print('Error traer sku')
    return image
