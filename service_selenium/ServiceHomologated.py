from concurrent.futures import ThreadPoolExecutor
from controller.DBController import get_retailer_homologated
from service_selenium.SamsClub import start_homologated


def start_scrap_homologated():
    # try:
    executor = ThreadPoolExecutor(max_workers=2)

    dataframe = get_retailer_homologated("SAM\'S CLUB")
    for i, date in dataframe.iterrows():
        executor.submit(start_homologated(date[1], date))

    dataframe = get_retailer_homologated("VERIZON")
    for i, date in dataframe.iterrows():
        executor.submit(start_homologated(date[1], date))

    # except Exception as e:
        #print(f'error en ServiceHomologated: {e}')
