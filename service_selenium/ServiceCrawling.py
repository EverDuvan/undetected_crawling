from concurrent.futures import ThreadPoolExecutor
from controller.DBController import get_retailer_crawling
from service_selenium.SamsClub import start_crawling


def start_scrap_crawling():
    # try:
    executor = ThreadPoolExecutor(max_workers=1)

    dataframe = get_retailer_crawling("verizon")
    for i, df in dataframe.iterrows():
        executor.submit(start_crawling(df))

    # except Exception as e:
        #print(f'error en ServiceHomologated: {e}')
