#from concurrent.futures import ThreadPoolExecutor
import pandas as pd

from controller.DataframeController import SetDateFrame
from controller.DBController import get_retailer_homologated
from service_selenium.SamsClub import start_homologated


def start_scrap_homologated():
    try:
        product = pd.DataFrame()
        #executor = ThreadPoolExecutor(max_workers=1)

        dataframe = get_retailer_homologated("SAMS CLUB")
        for i, df in dataframe.iterrows():
            #date_product = executor.submit(start_homologated(df))
            date_product = start_homologated(df)
            product = product.append(date_product, ignore_index=True)
            SetDateFrame(product, 'product_details',
                         'psql_write').send_df_replace  # PRODUCTO A PRODUCTO

        print("DATAFRAME LLENO >>>> "+product)
        product.to_csv('product.csv', index=False)
        # SetDateFrame(product, 'product_details', 'psql_write').send_df_replace #TODOS LOS PRODUCTOS
    except Exception as e:
        print(
            f'error en start_scrap_homologated in ServiceHomologated.py: {e}')
