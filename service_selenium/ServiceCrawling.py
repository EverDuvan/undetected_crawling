#from concurrent.futures import ThreadPoolExecutor
import pandas as pd

from controller.DBController import get_retailer_crawling
from service_selenium.SamsClub import start_crawling
from controller.DataframeController import SetDateFrame


def start_scrap_crawling():
    try:
        product = pd.DataFrame()
        #executor = ThreadPoolExecutor(max_workers=1)

        #dataframe = get_retailer_crawling("samsclub")
        #for i, df in dataframe.iterrows():
        product = start_crawling(None)

        print("DATAFRAME LLENO >>>> "+product)
        product = product.duplicated(product.columns[~product.columns.isin(['URL'])])
        SetDateFrame(product, 'product_details', 'psql_write').send_df_append
    except Exception as e:
        print(f'error en start_scrap_crawling in ServiceCrawling.py: {e}')
