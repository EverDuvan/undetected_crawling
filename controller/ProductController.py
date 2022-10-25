import pandas as pd


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

        date_product = {
            'PAIS': clean_attr(dataframe[2].upper()),
            'CATEGORIA':  clean_attr(dataframe[3].upper()),
            'SUBCATEGORIA':  clean_attr(dataframe[4].upper()),
            'WEB_NAME':  clean_attr(dataframe[5].upper()),
            'RETAILER':  clean_attr(dataframe[5].upper()),
            'URL': url.strip(),
            'DESCRIPTIONB':  clean_attr(name),
            'PRICE':  clean_attr(price),
            'DESCRIPTIONBF':  clean_attr(desc),
            'SKU':  clean_attr(sku),
            'SEGMENTO4':  clean_attr(stock),
            'MARCA':  clean_attr(new_brand),
            'MODELO_RETAILER':  clean_attr(new_model),
            'IMAGE':  clean_attr(image),
            'ROW_ID': 0,
            'CYCLE_ID': 0,
            'SEGMENTO1': 'NULL',
            'SEGMENTO2': 'NULL',
            'SEGMENTO3': 'NULL',
            'SEGMENTO5': 'NULL'
        }
        return date_product
    except Exception as e:
        print(f'error en save_product() in ProductController.py: {e}')


def clean_attr(attr):
    clean_attr = ''
    try:
        clean_attr = attr.replace('\n', ' ').strip()
        if clean_attr == None or clean_attr == '':
            clean_attr = ''
        else:
            if len(attr) > 250:
                clean_attr = attr[:249]
    except Exception as e:
        print(f'error en clean_attr() in ProductController.py: {e}')
    return clean_attr
