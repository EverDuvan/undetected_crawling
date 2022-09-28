import psycopg2
import mysql.connector
from Properties import *

class Datasheet:

    def __init__(self, id, country, retail, countryRetail, category, subcategory, urlCategory, webName):
        self.id = id
        self.country = country
        self.retail = retail
        self.countryRetail = countryRetail
        self.category = category
        self.subcategory = subcategory
        self.urlCategory = urlCategory
        self.webName = webName


def Conexion():
 
    lita_crawling = []

    try:
        prop = Properties.get_executor()
        #conexion_psql = prop.get_conexion_psql()
        conexion = psycopg2.connect(
            host=str(prop['host']),
            database=str(prop['database']),
            user=str(prop['user']),
            password=str(prop['password']))

        cur = conexion.cursor()

        cur.execute("SELECT \"id\",\"country\",\"retail\",\"countryRetail\",\"category\",\"subcategory\",\"urlCategory\",\"webName\" " +
                    "FROM retail_information WHERE \"country\" IN ('USA') and \"retail\" in (E'SAM\\'S CLUB')")

        for id, country, retail, countryRetail, category, subcategory, urlCategory, webName in cur.fetchall():
            craw = Datasheet(id, country, retail, countryRetail,
                            category, subcategory, urlCategory, webName)
            lita_crawling.append(craw)
            print(craw.urlCategory)

        conexion.close()

    except Exception as e:
        print(f'error en conexion(): {e}')

    return lita_crawling


def guardarDB(producto):

    try:

        db_connection = mysql.connector.connect(
            host="localhost",
            user="scrap_writer",
            password="U%awK0*%a2t6%2WTJ",
            port="3306",
            database='full_Web_Scraper'
        )

        cursor = db_connection.cursor()
        sql = 'INSERT INTO product_details (URL, PAIS, CATEGORIA, SUBCATEGORIA, RETAILER, MARCA, MODELO_RETAILER, MODELO_HITCH, DESCRIPTIONB, DESCRIPTIONF, PRICE, IMAGE, WEB_NAME, SKU) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)'
        val = (producto.productUrl,
            producto.pais,
            producto.categoria,
            producto.subcategoria,
            producto.webSiteName,
            producto.brandName,
            producto.modelCode,
            producto.modeloHitch,
            producto.productName,
            producto.description,
            producto.price,
            producto.images,
            producto.retailWeb,
            producto.sku)
        cursor.execute(sql, val)
        db_connection.commit()
        cursor.close()
        db_connection.close()

    except Exception as e:
        print(f'error en guardarDB(): {e}')
