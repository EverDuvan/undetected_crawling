from concurrent.futures import ThreadPoolExecutor
from controller.DBController import get_retailer_homologated
from service_selenium.SamsClub import start_homologated


def start_scrap_homologated():
    # try:
    executor = ThreadPoolExecutor(max_workers=1)

    dataframe = get_retailer_homologated("SAMS CLUB")
    for i, df in dataframe.iterrows():
        executor.submit(start_homologated(df))

    # except Exception as e:
        #print(f'error en ServiceHomologated: {e}')
