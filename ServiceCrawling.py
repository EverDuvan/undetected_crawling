from concurrent.futures import ThreadPoolExecutor
from DBController import *
from SamsClub import start_crawling



if __name__ == '__main__':

    try:

        executor = ThreadPoolExecutor(max_workers=2)
        list_datasheet = DBController.get_retailers_crawling()

        for datasheet in list_datasheet:
            executor.submit(start_crawling, datasheet)

    except Exception as e:
        print(f'error en main: {e}')
