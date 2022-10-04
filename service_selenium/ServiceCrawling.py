from concurrent.futures import ThreadPoolExecutor
from controller import DBController
from service_selenium import SamsClub

try:
    executor = ThreadPoolExecutor(max_workers=2)
    list_datasheet = DBController.get_retailers_crawling()
    for data_sheet in list_datasheet:
        web_name = data_sheet.web_name.lower().replace(' ', '')
        print(web_name)
        if web_name == 'samsclub':
            executor.submit(SamsClub.start_crawling(data_sheet))
except Exception as e:
    print(f'error en ServiceCrawling: {e}')
