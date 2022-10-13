import undetected_chromedriver as uc
from controller.ProxyController import get_proxy_random
from xvfbwrapper import Xvfb
import time


def start_driver():
    driver = None
    try:
        vdisplay = Xvfb(width=800, height=1280)
        vdisplay.start()
        options = uc.ChromeOptions()
        options.add_argument(
            '--no-first-run --no-service-autorun --password-store=basic')
        options.add_argument(f'--disable-gpu')
        options.add_argument(f'--no-sandbox')
        options.add_argument(f'--disable-dev-shm-usage')
        options.add_argument('--proxy-server=' + str(get_proxy_random()))
        CHROME_DRIVER_PATH = './chromedriver'
        driver = uc.Chrome(executable_path=CHROME_DRIVER_PATH,
                           options=options, headless=False)
    except Exception as e:
        print(f'error en start_driver() in SeleniumController.py: {e}')
    return driver


def open_url(url, driver):
    try:
        driver.get(url)
        time.sleep(5)
    except Exception as e:
        print(f'error en open_url() in SeleniumController.py: {e}')


def close_quit_driver(driver):
    try:
        driver.close()
        driver.quit()
    except Exception as e:
        print(f'error en close_quit_driver() in SeleniumController.py: {e}')
