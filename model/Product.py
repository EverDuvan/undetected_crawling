from model.DataSheet import DataSheet


class Product:

    def __init__(self, dataframe, url, name, price, description, sku, stock, brand, model, image):
        self.country = dataframe[2].upper()
        self.category = dataframe[3].upper()
        self.sub_category = dataframe[4].upper()
        self.web_name = dataframe[5].upper()
        self.retail = dataframe[5].upper()
        self.url = url.strip()
        self.name = name.strip()
        self.price = price.strip()
        self.description = description.strip().replace('\n', ' ')
        self.sku = sku.strip()
        self.stock = stock.strip()
        if self.dataframe[6].brand != None:
            self.brand = dataframe[6]
        else:
            self.brand = brand.strip()
        if self.dataframe[7] != None:
            self.model = dataframe[7]
        else:
            self.model = model.strip()
        self.image = image.strip()
