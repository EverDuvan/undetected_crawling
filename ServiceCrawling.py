from concurrent.futures import ThreadPoolExecutor
from DBController import Conexion
from SamsClub import *


if __name__ == '__main__':

    try:

        executor = ThreadPoolExecutor(max_workers=2)
        list_datasheet = Conexion()

        for datasheet in list_datasheet:
            executor.submit(start_crawling, datasheet)

    except Exception as e:
        print(f'error en main: {e}')
