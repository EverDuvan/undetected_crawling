from selenium.webdriver.common.by import By
from controller.SeleniumController import start_driver, open_url, close_quit_driver
from controller.PriceController import clean_price
from controller.ProductController import save_product


def start_crawling(product, dateframe):
    try:
        urls = []
        driver = start_driver()
        if driver != None:
            urls = get_urls(driver, dateframe[6], 0)
            close_quit_driver(driver)

        for url in urls:
            date_product = get_details(url, dateframe)
            product = product.append(date_product, ignore_index=True)
        return product
    except Exception as e:
        print(f'error en start_crawling() in SamsClub.py: {e}')


def start_homologated(dataframe):
    try:
        date_product = get_details(dataframe[1], dataframe)
        return date_product
    except Exception as e:
        print(f'error en start_homologated() in SamsClub.py: {e}')


def get_urls(driver, url, page_count):
    urls = []
    try:
        load = True
        have_product = False
        while(load):
            if page_count == 0:
                open_url(driver, url)
            else:
                open_url(f'{driver}{url}?offset={str(page_count)}')
            if len(driver.find_elements(By.CSS_SELECTOR, 'div.sc-pc-medium-desktop-card>a')) > 0:
                elements = driver.find_elements(
                    By.CSS_SELECTOR, 'div.sc-pc-medium-desktop-card>a')
                for element in elements:
                    href = element.get_attribute('href')
                    if href != None and href != '' and href not in urls:
                        urls.append(href)
                        have_product = True
                if have_product:
                    page_count = page_count+45
                    have_product = False
                else:
                    load = False
            else:
                load = False
    except Exception as e:
        print(f'error en get_urls() in SamsClub.py: {e}')
    return urls


def get_details(url, dataframe):
    try:
        driver = start_driver()
        if driver != None:
            open_url(driver, url)
            name = get_name(driver)
            if name != None:
                price = clean_price(get_price(driver), '$')
                sku = get_sku(driver)
                stock = get_stock(driver)
                brand = get_brand(driver)
                model = get_model(driver)
                image = get_image(driver)
                date_product = save_product(dataframe, url, name, price, name,
                                            sku, stock, brand, model, image)
                print('------------------------------------------')
                print(f'URL > {url}')
                print(f'NAME > {name}')
                print(f'PRICE > {price}')
                print(f'PRICE SIN LIMPIAR > {get_price(driver)}')
                print(f'SKU > {sku}')
                print(f'STOCK > {stock}')
                print(f'BRAND > {brand}')
                print(f'MODEL > {model}')
                print(f'IMAGE > {image}')
                print('------------------------------------------')
        close_quit_driver(driver)
        return date_product
    except Exception as e:
        print(f'error en get_details() in SamsClub.py: {e}')


def get_name(driver):
    name = ''
    try:
        if len(driver.find_elements(By.XPATH, '//h1')) > 0:
            name = driver.find_element(By.XPATH, '//h1').text
    except Exception as e:
        name = ''
    return name


def get_price(driver):
    price = ''
    try:
        if len(driver.find_elements(By.CSS_SELECTOR, 'meta[itemprop=\'price\']')) > 0:
            price = driver.find_element(
                By.CSS_SELECTOR, 'meta[itemprop=\'price\']').get_attribute('content')
    except Exception as e:
        price = ''
    return price


def get_sku(driver):
    sku = ''
    try:
        if len(driver.find_elements(By.XPATH, '//meta[contains(@itemprop, \"sku\")]')) > 0:
            sku = driver.find_element(
                By.XPATH, '//meta[contains(@itemprop, \"sku\")]').get_attribute('content')
    except Exception as e:
        sku = ''
    return (sku)


def get_stock(driver):
    stock = 'true'
    try:
        if len(driver.find_elements(By.XPATH, '//meta[contains(@itemprop, \"availability\")]')) > 0:
            reference = driver.find_element(
                By.XPATH, '//meta[contains(@itemprop, \"availability\")]').get_attribute('content')
        if reference != 'InStock':
            stock = 'false'
    except Exception as e:
        stock = 'true'
    return (stock)


def get_brand(driver):
    brand = ''
    try:
        if len(driver.find_elements(By.CSS_SELECTOR, 'span.sc-product-header-item-number')) > 0:
            brand = driver.find_element(
                By.CSS_SELECTOR, 'span.sc-product-header-item-number').text
            if 'By' in brand:
                brand = brand.replace('By', '').strip()
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
