from DataSheet import DataSheet


class Product:

    def __init__(self, data_sheet: DataSheet, url, name, price, description, sku, stock, brand, model, image):
        self.country = data_sheet.country.upper()
        self.category = data_sheet.category.upper()
        self.sub_category = data_sheet.sub_category.upper()
        self.web_name = data_sheet.web_name.upper()
        self.retail = data_sheet.retail.upper()
        self.url = url.strip()
        self.name = name.strip()
        self.price = price.strip()
        self.description = description.strip().replace('\n', ' ')
        self.sku = sku.strip()
        self.stock = stock.strip()
        if data_sheet.brand != None:
            self.brand = data_sheet.brand
        else:
            self.brand = brand.strip()
        if self.data_sheet.model != None:
            self.model = data_sheet.model
        else:
            self.model = model.strip()
        self.image = image.strip()
