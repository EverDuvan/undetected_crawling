import undetected_chromedriver as uc
from controller import ProxyController
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
        options.add_argument('--proxy-server=' +
                             str(ProxyController.get_proxy_random()))
        CHROME_DRIVER_PATH = '/usr/bin/chromedriver'
        driver = uc.Chrome(executable_path=CHROME_DRIVER_PATH,
                           options=options, headless=False)
    except Exception as e:
        driver = None
        print(f'error en start_driver(): {e}')
    return driver

def open_url(url, driver):
    try:
        driver.get(url)
        time.sleep(5)
    except Exception as e:
        print(f'error en open_url(): {e}')
