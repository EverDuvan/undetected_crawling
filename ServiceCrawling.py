from concurrent.futures import ThreadPoolExecutor
from DBController import *
from SamsClub import start_crawling


if __name__ == '__main__':
    try:
        executor = ThreadPoolExecutor(max_workers=2)
        list_datasheet = DBController.get_retailers_crawling()
        for data_sheet in list_datasheet:
            web_name = data_sheet.web_name.lower().replace('\'', '').replace(' ', '')
            print(web_name)
            if(web_name == 'samsclub'):
                executor.submit(start_crawling(data_sheet))
    except Exception as e:
        print(f'error en main: {e}')
