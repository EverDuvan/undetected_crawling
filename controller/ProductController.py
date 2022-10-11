import pandas as pd

from controller.DataframeController import SetDateFrame


class ProductController:
    product = None

    def __init__(self):
        self.product = pd.DataFrame()

    def save_product(self, dataframe, url, name, price, desc, sku, stock, brand, model, image):
        try:
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
            self.product = self.product.append(date_product, ignore_index=True)
        except Exception as e:
            print(f'error en save_product(): {e}')
        print(self.product)