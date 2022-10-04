from controller import PropertieController
from service_selenium import ServiceCrawling, ServiceHomologated

if __name__ == '__main__':
    try:
        prop = PropertieController.get_executor('configuration')
        mood = str(prop['mood'])
        if mood == "homologated":
            ServiceHomologated()
        else:
            ServiceCrawling()
    except Exception as e:
        print(f'error en main principal: {e}')
