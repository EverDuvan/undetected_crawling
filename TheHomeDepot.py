import pandas as pd

from selenium.webdriver.common.by import By
from controller.SeleniumController import start_driver, open_url, close_quit_driver
from controller.PriceController import clean_price
from controller.ProductController import save_product


def start_crawling(product, dateframe):
    try:
        urls = []
        driver = start_driver()
        if driver != None:
            urls = get_urls(driver, 'https://www.homedepot.com/b/Heating-Venting-Cooling-Fireplaces/N-5yc1vZc4lb?catStyle=ShowProducts')
            close_quit_driver(driver)

        for url in urls:
            date_product = get_details(url, dateframe)
            product = product.append(date_product, ignore_index=True)
        print(f'product : {product}')
        return product
    except Exception as e:
        print(f'error en start_crawling() in SamsClub.py: {e}')


def start_homologated(dataframe):
    try:
        date_product = get_details(dataframe[1], dataframe)
        return date_product
    except Exception as e:
        print(f'error en start_homologated() in SamsClub.py: {e}')


def get_urls(driver, url):
    urls = []
    try:
        load = True
        have_product = False
        open_url(driver, url)

        while (load):
            if len(driver.find_elements(By.CSS_SELECTOR, 'a.header.product-pod--ie-fix')) > 0:
                elements = driver.find_elements(
                    By.CSS_SELECTOR, 'a.header.product-pod--ie-fix')
                for element in elements:
                    href = element.get_attribute('href')
                    if href != None and href != '' and href not in urls:
                        urls.append(href)
                        have_product = True
                if have_product:
                    have_product = False
                else:
                    load = False
            else:
                load = False
    except Exception as e:
        print(f'error en get_urls() in {e}')
    return urls


def get_details(url, dataframe):
    try:
        driver = start_driver()
        if driver != None:
            open_url(driver, url)
            name = get_name(driver)
            if name != None:
                price = clean_price(get_price(driver), '$')
                print('price ' + price)
                desc = get_description(driver)
                sku = get_sku(driver)
                brand = get_brand(driver)
                model = get_model(driver)
                image = get_image(driver)
                date_product = save_product(dataframe, url, name, price, desc,
                                            sku, '', brand, model, image)
        close_quit_driver(driver)
        return date_product
    except Exception as e:
        print(f'error en get_details() in SamsClub.py: {e}')


def get_name(driver):
    name = ''
    try:
        if len(driver.find_elements(By.CSS_SELECTOR, 'h1.product-details__title')) > 0:
            name = driver.find_element(
                By.CSS_SELECTOR, 'h1.product-details__title').text
        if len(driver.find_elements(By.CSS_SELECTOR, 'h1[itemprop=name]')) > 0 and name == "":
            name = driver.find_element(
                By.CSS_SELECTOR, 'h1[itemprop=name]').text
    except Exception as e:
        name = ''
    return name


def get_price(driver):
    price = ''
    try:
        if len(driver.find_elements(By.CSS_SELECTOR, 'meta[itemprop=price]')) > 0:
            price = driver.find_element(
                By.CSS_SELECTOR, 'meta[itemprop=price]').get_attribute('content')
    except Exception as e:
        price = ''
    return price


def get_description(driver):
    desc = ''
    try:
        list = []
        if len(driver.find_elements(By.CSS_SELECTOR, 'div.sc-description-about-long>p')) > 0:
            elements = driver.find_elements(
                By.CSS_SELECTOR, 'div.sc-description-about-long>p')
            for element in elements:
                list.append(element.text)
            desc = ', '.join(list)
    except Exception as e:
        desc = ''
    return desc


def get_sku(driver):
    sku = ''
    try:
        if len(driver.find_elements(By.XPATH, '//meta[contains(@itemprop, \"sku\")]')) > 0:
            sku = driver.find_element(
                By.XPATH, '//meta[contains(@itemprop, \"sku\")]').get_attribute('content')
    except Exception as e:
        sku = ''
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
        brand = ''
    return brand


def get_model(driver):
    model = ''
    try:
        if len(driver.find_elements(By.XPATH, '//meta[contains(@itemprop, \"mpn\")]')) > 0:
            model = driver.find_element(
                By.XPATH, '//meta[contains(@itemprop, \"mpn\")]').get_attribute('content')
    except Exception as e:
        model = ''
    return model


def get_image(driver):
    image = ''
    try:
        if len(driver.find_elements(By.XPATH, '//meta[contains(@property, \"og:image\")]')) > 0:
            image = driver.find_element(
                By.XPATH, '//meta[contains(@property, \"og:image\")]').get_attribute('content')
    except Exception as e:
        image = ''
    return image


if __name__ == '__main__':
    get_details('https://cr.siman.com/audifono-inalambrico-con-microfono-skullcandy-inkd-102363617/p',None)
    #start_crawling(None,None)
