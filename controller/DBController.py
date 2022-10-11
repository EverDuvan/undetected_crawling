from builtins import print
from controller.DataframeController import GetDataFrame
from controller.PropertieController import get_countries, get_retailers

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
