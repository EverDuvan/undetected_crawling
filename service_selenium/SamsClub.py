from selenium.webdriver.common.by import By
from model.Product import Product
#from controller.DBController import DBController
from controller.SeleniumController import start_driver, open_url, close_quit_driver


def start_crawling(data_sheet):
    try:
        urls = []
        driver = start_driver()
        if driver != None:
            urls = get_urls(driver, data_sheet.url)
            close_quit_driver(driver)

        for url in urls:
            start_homologated(url, data_sheet)
    except Exception as e:
        print(f'error en start_crawling(): {e}')


def get_urls(driver, url):
    urls = []
    try:
        open_url(url, driver)
        if len(driver.find_elements(By.CSS_SELECTOR, 'div.sc-pc-medium-desktop-card > a')) > 0:
            elements = driver.find_elements(
                By.CSS_SELECTOR, 'div.sc-pc-medium-desktop-card > a')
        for element in elements:
            urls.append(element.get_attribute('href'))
    except Exception as e:
        print(f'error en get_urls(): {e}')
    return urls


def start_homologated(url, data_sheet):
    try:
        driver = start_driver()
        if driver != None:
            open_url(url, driver)
            name = get_name(driver)
            if name != None:
                price = get_price(driver)
                description = get_description(driver)
                sku = get_sku(driver)
                brand = get_brand(driver)
                model = get_model(driver)
                image = get_image(driver)
                #product = Product(data_sheet, url, name, price,
                #                  description, sku, '', brand, model, image)
                # DBController.save_product(product)
            print('---------------')
            print(url)
            print(name)
            print(price)
            close_quit_driver(driver)
    except Exception as e:
        print(f'error en start_homologated(): {e}')


def get_name(driver):
    name = ''
    try:
        if len(driver.find_elements(By.XPATH, '//h1')) > 0:
            name = driver.find_element(By.XPATH, '//h1').text
    except Exception as e:
        print(f'error en get_name(): {e}')
    return name


def get_price(driver):
    price = ''
    try:
        if len(driver.find_elements(By.XPATH, '//meta[contains(@itemprop, \"price\")]')) > 0:
            price = driver.find_element(
                By.XPATH, '//meta[contains(@itemprop, \"price\")]').get_attribute('content')
    except Exception as e:
        print(f'error en get_price(): {e}')
    return price


def get_description(driver):
    desc = ''
    try:
        list = []
        if len(driver.find_elements(By.CSS_SELECTOR, 'div.sc-description-about-long')) > 0:
            elements = driver.find_elements(
                By.CSS_SELECTOR, 'div.sc-description-about-long > p')
            for element in elements:
                list.append(element.text)
            desc = ', '.join(list)
    except Exception as e:
        print(f'error en get_description(): {e}')
    return desc


def get_sku(driver):
    sku = ''
    try:
        if len(driver.find_elements(By.XPATH, '//meta[contains(@itemprop, \"sku\")]')) > 0:
            sku = driver.find_element(
                By.XPATH, '//meta[contains(@itemprop, \"sku\")]').get_attribute('content')
    except Exception as e:
        print(f'error en get_sku(): {e}')
    return (sku)


def get_brand(driver):
    brand = ''
    try:
        if len(driver.find_elements(By.CSS_SELECTOR, 'span.sc-product-header-item-number')) > 0:
            brand = driver.find_element(
                By.CSS_SELECTOR, 'span.sc-product-header-item-number').text
            if "By" in brand:
                brand = brand.replace("By", "").strip()
    except Exception as e:
        print(f'error en get_brand(): {e}')
    return brand


def get_model(driver):
    model = ''
    try:
        if len(driver.find_elements(By.XPATH, '//meta[contains(@itemprop, \"mpn\")]')) > 0:
            model = driver.find_element(
                By.XPATH, '//meta[contains(@itemprop, \"mpn\")]').get_attribute('content')
    except Exception as e:
        print(f'error en get_model(): {e}')
    return model


def get_image(driver):
    image = ''
    try:
        if len(driver.find_elements(By.XPATH, '//meta[contains(@property, \"og:image\")]')) > 0:
            image = driver.find_element(
                By.XPATH, '//meta[contains(@property, \"og:image\")]').get_attribute('content')
    except Exception as e:
        print(f'error en get_image(): {e}')
    return image