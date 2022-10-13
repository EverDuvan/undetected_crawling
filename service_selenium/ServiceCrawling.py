from concurrent.futures import ThreadPoolExecutor
from controller.ProductController import *
from controller.DBController import get_retailer_crawling
from service_selenium.SamsClub import start_crawling
from controller.DataframeController import SetDateFrame

p = ProductController()


def start_scrap_crawling():
    try:
        executor = ThreadPoolExecutor(max_workers=1)

        dataframe = get_retailer_crawling("samsclub")
        for i, df in dataframe.iterrows():
            executor.submit(start_crawling(df))

        # SetDateFrame(p.product, 'product_details',
            # 'conexion_mysql').send_df_append
    except Exception as e:
        print(f'error en start_scrap_crawling in ServiceCrawling.py: {e}')
