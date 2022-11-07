import psycopg2
from builtins import print
from controller.DataframeController import GetDataFrame
from controller.PropertieController import get_executor, get_countries, get_retailers

countries = eval(get_countries())
retailers = eval(get_retailers())


def get_dataframe_crawling():
    try:
        dataframe = GetDataFrame('retail_information',
                                 'psql_read').get_dataframe
        dataframe = dataframe[dataframe['country'].isin(countries)]
        dataframe = dataframe[dataframe['retail'].isin(retailers)]
        return dataframe
    except Exception as e:
        print(f'error en get_dataframe_crawling() in DBController.py: {e}')


def get_retailer_crawling(web_name):
    try:
        dataframe = get_dataframe_crawling()
        dataframe = dataframe[dataframe['webName'] == web_name]
        return dataframe
    except Exception as e:
        print(f'error en get_retailer_crawling() in DBController.py: {e}')


def get_dataframe_homologated():
    try:
        dataframe = GetDataFrame('product_homologated',
                                 'psql_read').get_dataframe
        dataframe = dataframe[dataframe['PAIS'].isin(countries)]
        dataframe = dataframe[dataframe['RETAILER'].isin(retailers)]
        return dataframe
    except Exception as e:
        print(f'error en get_dataframe_homologated() in DBController.py: {e}')


def get_retailer_homologated(web_name):
    try:
        dataframe = get_dataframe_homologated()
        dataframe = dataframe[dataframe['RETAILER'] == web_name]
        return dataframe
    except Exception as e:
        print(f'error en get_dataframe_homologated() in DBController.py: {e}')


def truncate_table():
    prop = get_executor('psql_write')
    connection = psycopg2.connect(host=str(prop['host']), database=str(
        prop['database']), user=str(prop['user']), password=str(prop['password']), port=str(prop['port']))
    cur = conection.cursor()
    cur.execute('TRUNCATE TABLE product_details')
    cur.close()
    connection.close()
    except Exception as e:
        print(f'error en truncate_table(): {e}')
