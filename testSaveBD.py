from concurrent.futures import process
from itertools import product
import mysql.connector


def guardarDB(producto):

    db_connection = mysql.connector.connect(
        host="localhost",
        user="scrap_writer",
        password="U%awK0*%a2t6%2WTJ",
        port="3306",
        database='full_Web_Scraper'
    )

    cursor = db_connection.cursor()
    sql = 'INSERT INTO product_details (URL, PAIS, CATEGORIA, SUBCATEGORIA, RETAILER, MARCA, MODELO_RETAILER, MODELO_HITCH, DESCRIPTIONB, DESCRIPTIONF, PRICE, IMAGE, WEB_NAME, SKU) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)'
    #sql = 'INSERT INTO product_details (URL, PAIS, DESCRIPTIONB) VALUES (%s, %s, %s)'
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
