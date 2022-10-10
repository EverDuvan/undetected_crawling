from controller.DataframeController import GetDataFrame
from controller.PropertieController import get_countries, get_retailers
import pandas as pd

date_product = {'country': ['default'], 'category': ['default'], 'sub_category': ['default'], 'web_name': ['default'],
                'retail': ['default'], 'url': ['default'], 'name': ['default'], 'price': ['default'], 'description': ['default'],
                'sku': ['default'], 'stock': ['default'], 'brand': ['default'], 'model': ['default'], 'image': ['default']}
product = pd.DataFrame(date_product)

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


def save_product(dataframe, url, name, price, desc, sku, stock, brand, model, image):
    print(product)
    new_brand = ''
    if dataframe[6] != None:
        new_brand = dataframe[6]
    else:
        new_brand = brand.strip()
    new_model = ''
    if dataframe[7] != None:
        new_model = dataframe[7]
    else:
        new_model = model.strip()
    date_product = {'country': dataframe[2].upper(), 'category': dataframe[3].upper(), 'sub_category': dataframe[4].upper(), 'web_name': dataframe[5].upper(),
                    'retail': dataframe[5].upper(), 'url': url.strip(), 'name': name.strip(), 'price': price.strip(), 'description': desc.strip().replace('\n', ' '),
                    'sku': sku.strip(), 'stock': stock.strip(), 'brand': new_brand, 'model': new_model, 'image': image}
    product = product.concat(date_product, ignore_index=True)
    print(product)
