import pandas as pd

#from controller.DataframeController import SetDateFrame


def save_product(dataframe, url, name, price, desc, sku, stock, brand, model, image):
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

        date_product = {'PAIS': dataframe[2].upper(), 'CATEGORIA': dataframe[3].upper(), 'SUBCATEGORIA': dataframe[4].upper(), 'WEB_NAME': dataframe[5].upper(),
                        'RETAILER': dataframe[5].upper(), 'URL': url.strip(), 'DESCRIPTIONB': name.strip(), 'PRICE': price.strip(), 'DESCRIPTIONBF': desc.strip().replace('\n', ' '),
                        'SKU': sku.strip(), 'SEGMENTO4': stock.strip(), 'MARCA': new_brand, 'MODELO_RETAILER': new_model, 'IMAGE': image}
        return date_product
    except Exception as e:
        print(f'error en save_product() in ProductController.py: {e}')
