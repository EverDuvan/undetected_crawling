#from concurrent.futures import ThreadPoolExecutor
import pandas as pd

from controller.DataframeController import SetDateFrame
from controller.DBController import get_retailer_crawling
from service_selenium.SamsClub import start_crawling


def start_scrap_crawling():
    try:
        product = pd.DataFrame()
        #executor = ThreadPoolExecutor(max_workers=1)

        dataframe = get_retailer_crawling("samsclub")
        for i, df in dataframe.iterrows():
            product = start_crawling(product,df)
            print(f'DATAFRAME LLENO >>>> {product}')
            product.to_csv('product.csv', index=False)
            SetDateFrame(product, 'product_details', 'psql_write').send_df_append
    except Exception as e:
        print(f'error en start_scrap_crawling in ServiceCrawling.py: {e}')

