from concurrent.futures import ThreadPoolExecutor
from controller.DBController import *
from SamsClub import start_homologated


try:
    executor = ThreadPoolExecutor(max_workers=2)
    list_datasheet = DBController.get_retailers_homologated()
    for data_sheet in list_datasheet:
        web_name = data_sheet.web_name.lower().replace('\'', '').replace(' ', '')
        print(web_name)
        if(web_name == 'samsclub'):
            executor.submit(start_homologated(data_sheet.url, data_sheet))
except Exception as e:
    print(f'error en ServiceHomologated: {e}')
