import undetected_chromedriver as uc
from controller.ProxyController import get_proxy_random
from xvfbwrapper import Xvfb
import time


def start_driver():
    driver = None
    try:
        user_agent = 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/107.0.5304.68 Safari/537.36'
        vdisplay = Xvfb(width=800, height=1280)
        vdisplay.start()
        options = uc.ChromeOptions()
        options.add_argument(
            '--no-first-run --no-service-autorun --password-store=basic')
        options.add_argument(f'--disable-gpu')
        options.add_argument(f'--no-sandbox')
        options.add_argument(f'--disable-dev-shm-usage')
        options.add_argument(f'--user-agent='+str(user_agent))
        options.add_argument(f'--proxy-server=%s' + str(get_proxy_random()))
        CHROME_DRIVER_PATH = './chromedriver'
        driver = uc.Chrome(executable_path=CHROME_DRIVER_PATH,
                           options=options, headless=False)
    except Exception as e:
        print(f'error en start_driver() in SeleniumController.py: {e}')
    return driver


def open_url(driver, url):
    try:
        if driver != None:
            driver.get(str(url))
            time.sleep(20)
    except Exception as e:
        print(f'error en open_url() in SeleniumController.py: {e}')


def close_quit_driver(driver):
    try:
        if driver != None:
            driver.close()
            driver.quit()
    except Exception as e:
        print(f'error en close_quit_driver() in SeleniumController.py: {e}')
