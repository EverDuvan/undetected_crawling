import psycopg2
import mysql.connector
from DataSheet import *
from Properties import *


class DBController:

    connection_psql = None
    connection_mysql = None

    @classmethod
    def get_connection_psql(cls):
        try:
            if cls.connection_psql != None:
                return cls.connection_psql
            else:
                prop = Properties.get_executor('conexion_psql')
                cls.connection_psql = psycopg2.connect(
                    host=str(prop['host']),
                    database=str(prop['database']),
                    user=str(prop['user']),
                    password=str(prop['password']))
                return cls.connection_psql
        except Exception as e:
            print(f'error en get_connection_psql(): {e}')

    @classmethod
    def get_connection_mysql(cls):
        try:
            if cls.connection_mysql != None:
                return cls.connection_mysql
            else:
                prop = Properties.get_executor('conexion_mysql')
                cls.connection_mysql = mysql.connector.connect(
                    host=str(prop['host']),
                    database=str(prop['database']),
                    user=str(prop['user']),
                    password=str(prop['password']),
                    port=str(prop['password']))
                return cls.connection_mysql
        except Exception as e:
            print(f'error en get_connection_mysql(): {e}')

    @classmethod
    def get_retailers_crawling(cls):
        list_crawling = []
        try:
            countries = Properties.get_countries()
            retailers = Properties.get_retailers()

            conection = cls.get_connection_psql()
            cur = conection.cursor()
            cur.execute("SELECT * FROM retail_information WHERE country IN ({}) and retail in ({})".format(
                str(countries), str(retailers)))

            for row in cur.fetchall():
                list_crawling.append(
                    DataSheet(row[0], row[1], row[2], row[3], row[4], row[5], row[6], row[7], '', ''))
            cur.close()
            cls.connection_psql.close()

        except Exception as e:
            print(f'error en get_retailers_crawling(): {e}')
        return list_crawling

    @classmethod
    def get_retailers_homologated(cls):
        list_homologated = []
        try:
            countries = Properties.get_countries()
            retailers = Properties.get_retailers()

            conection = cls.get_connection_psql()
            cur = conection.cursor()
            cur.execute("SELECT * FROM product_homologated WHERE \"PAIS\" IN ({}) AND \"RETAILER\" IN ({})".format(
                str(countries), str(retailers)))
            print(str(countries), str(retailers))
            for row in cur.fetchall():
                list_homologated.append(
                    DataSheet(row[0], row[2], row[5], row[2], row[3], row[4], row[1], row[5], row[6], row[7]))
            cur.close()
            cls.connection_psql.close()

        except Exception as e:
            print(f'error en get_retailers_homologated(): {e}')
        return list_homologated

    @classmethod
    def save_product(cls, product):
        try:
            cursor = cls.connection_mysql.cursor()
            sql = 'INSERT INTO product_details (PAIS, CATEGORIA, SUBCATEGORIA, WEB_NAME, RETAILER, URL, DESCRIPTIONB, PRICE, DESCRIPTIONF, SKU, SEGMENTO4, MARCA, MODELO_RETAILER, IMAGE) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)'
            val = (product.country,
                   product.category,
                   product.sub_category,
                   product.web_name,
                   product.retail,
                   product.url,
                   product.name,
                   product.price,
                   product.description,
                   product.sku,
                   product.stock,
                   product.brand,
                   product.model,
                   product.image)
            cursor.execute(sql, val)
            cls.connection_mysql.commit()
            cursor.close()
            cls.connection_mysql.close()
        except Exception as e:
            print(f'error en save_product(): {e}')
