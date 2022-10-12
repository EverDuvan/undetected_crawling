from controller.PropertieController import get_executor
from service_selenium.ServiceHomologated import start_scrap_homologated
from service_selenium.ServiceCrawling import start_scrap_crawling

if __name__ == '__main__':
    try:
        prop = get_executor('configuration')
        mood = str(prop['mood'])
        if mood == "homologated":
            start_scrap_homologated()
        else:
            start_scrap_crawling()
    except Exception as e:
        print(f'error en main principal: {e}')
