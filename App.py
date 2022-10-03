from concurrent.futures import ThreadPoolExecutor

from Properties import Properties
from ServiceHomologated import ServiceHomologated
from ServiceCrawling import ServiceCrawling

if __name__ == '__main__':
    try:
        prop = Properties.get_executor('configuration')
        mood=str(prop['mood'])
        print(mood)
        if mood=="homologated":
            ServiceHomologated()
        else:
            ServiceCrawling()
    except Exception as e:
        print(f'error en main principal: {e}')