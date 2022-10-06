from controller.DataframeController import GetDataFrame
from controller.PropertieController import get_countries, get_retailers
import pandas as pd

product = pd.DataFrame()

def get_dataframe_crawling():
    countries = eval(get_countries())
    retailers = eval(get_retailers())
    print(countries)
    print(retailers)
    dataframe = GetDataFrame('retail_information',
                             'conexion_psql').get_dataframe
    dataframe = dataframe[dataframe['country'].isin(countries)]
    dataframe = dataframe[dataframe['retail'].isin(retailers)]
    return dataframe


def get_retailer_crawling(web_name):
    dataframe = get_dataframe_crawling()
    dataframe = dataframe[dataframe['webName'] == web_name]
    return dataframe


def get_dataframe_homologated():
    countries = eval(get_countries())
    retailers = eval(get_retailers())
    print(countries)
    print(retailers)
    dataframe = GetDataFrame('product_homologated',
                             'conexion_psql').get_dataframe
    dataframe = dataframe[dataframe['PAIS'].isin(countries)]
    dataframe = dataframe[dataframe['RETAILER'].isin(retailers)]
    return dataframe


def get_retailer_homologated(web_name):
    dataframe = get_dataframe_homologated()
    dataframe = dataframe[dataframe['RETAILER'] == web_name]
    return dataframe


def save_product(frame, url, name, price, desc, sku, stock, brand, model, image):
    product['country'] = frame[2].upper()
    product['category'] = frame[3].upper()
    product['sub_category'] = frame[4].upper()
    product['web_name'] = frame[5].upper()
    product['retail'] = frame[5].upper()
    product['url'] = url.strip()
    product['name'] = name.strip()
    product['price'] = price.strip()
    product['description'] = desc.strip().replace('\n', ' ')
    product['sku'] = sku.strip()
    product['stock'] = stock.strip()
    product['image'] = image.strip()
    if frame[6] != None:
        product['brand'] = frame[6]
    else:
        product['brand'] = brand.strip()
    if frame[7] != None:
        product['model'] = frame[7]
    else:
        product['model'] = model.strip()
    print(product)
