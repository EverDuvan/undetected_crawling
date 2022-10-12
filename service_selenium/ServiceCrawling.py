from concurrent.futures import ThreadPoolExecutor
from controller.ProductController import *
from controller.DBController import get_retailer_crawling
from controller.DataframeController import SetDateFrame
from service_selenium.SamsClub import start_crawling

p = ProductController()

def start_scrap_crawling():
    try:
        executor = ThreadPoolExecutor(max_workers=1)

        dataframe = get_retailer_crawling("samsclub")
        for i, df in dataframe.iterrows():
            executor.submit(start_crawling(df))

        SetDateFrame(p.product(),'','conexion_mysql')
    except Exception as e:
        print(f'error en start_scrap_crawling: {e}')
