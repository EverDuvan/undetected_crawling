from DataSheet import *
from DBController import *


class Product:

    country = ''
    category = ''
    sub_category = ''
    web_name = ''
    retail = ''
    url = ''
    name = ''
    price = ''
    description = ''
    sku = ''
    stock = ''
    brand = ''
    model = ''
    image = ''
    data_sheet = DataSheet()
    db_controller = DBController()

    @data_sheet.setter
    def data_sheet(cls, data_sheet ):
        cls.data_sheet = data_sheet
        cls.country = cls.data_sheet.country.upper()
        cls.category = cls.data_sheet.category.upper()
        cls.sub_category = cls.data_sheet.sub_category.upper()
        cls.web_name = cls.data_sheet.web_name.upper()
        cls.retail = cls.data_sheet.retail.upper()

    @url.setter
    def url(cls, url):
        cls._url = url.strip()

    @name.setter
    def name(cls, name):
        cls._name = name.strip()

    @price.setter
    def price(cls, price):
        cls._price = price.strip()

    @description.setter
    def description(cls, description):
        cls._description = description.strip().replace('\n',' ')

    @sku.setter
    def sku(cls, sku):
        cls._sku = sku.strip()

    @stock.setter
    def stock(cls, stock):
        cls._stock = stock.strip()

    @brand.setter
    def brand(cls, brand):
        if cls._data_sheet.brand != None:
            cls._brand = cls._data_sheet.brand
        else:
            cls._brand = brand.strip()

    @model.setter
    def model(cls, model):
        if cls._data_sheet.model != None:
            cls._model = cls._data_sheet.model
        else:
            cls._model = model.strip()

    @image.setter
    def image(cls, image):
        cls._image = image.strip()


    def save(cls, product):
        cls.db_controller.save_product(product)

