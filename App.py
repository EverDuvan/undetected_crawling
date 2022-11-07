from service_selenium.ServiceHomologated import start_scrap_homologated
from service_selenium.ServiceCrawling import start_scrap_crawling
from controller.DbController import truncate_table
from controller.PropertieController import get_executor

if __name__ == '__main__':
    try:
        trucate_table()
        prop = get_executor('configuration')
        mood = str(prop['mood'])
        if mood == "homologated":
            start_scrap_homologated()
        else:
            start_scrap_crawling()
    except Exception as e:
        print(f'error en main principal in App.py: {e}')
