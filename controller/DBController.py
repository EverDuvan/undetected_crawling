from controller.DataframeController import GetDataFrame
from controller.PropertieController import get_countries, get_retailers
import pandas as pd

product = pd.DataFrame()
countries = eval(get_countries())
retailers = eval(get_retailers())
print(countries)
print(retailers)


def get_dataframe_crawling():
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
    dataframe = GetDataFrame('product_homologated',
                             'conexion_psql').get_dataframe
    dataframe = dataframe[dataframe['PAIS'].isin(countries)]
    dataframe = dataframe[dataframe['RETAILER'].isin(retailers)]
    return dataframe


def get_retailer_homologated(web_name):
    dataframe = get_dataframe_homologated()
    dataframe = dataframe[dataframe['RETAILER'] == web_name]
    return dataframe


def save_product(df, url, name, price, desc, sku, stock, brand, model, image):
    if product != None:
        product['country'].append(df[2].upper())
        product['category'].append(df[3].upper())
        product['sub_category'].append(df[4].upper())
        product['web_name'].append(df[5].upper())
        product['retail'].append(df[5].upper())
        product['url'].append(url.strip())
        product['name'].append(name.strip())
        product['price'].append(price.strip())
        product['description'].append(desc.strip().replace('\n', ' '))
        product['sku'].append(sku.strip())
        product['stock'].append(stock.strip())
        if df[6] != None:
            product['brand'].append(df[6])
        else:
            product['brand'].append(brand.strip())
        if df[7] != None:
            product['model'].append(df[7])
        else:
            product['model'].append(model.strip())
        product['image'].append(image.strip())
        print(product)
