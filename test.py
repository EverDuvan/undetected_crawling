from io import BytesIO
import time
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import requests
import undetected_chromedriver as uc
from selenium.webdriver.common.by import By
from PIL import Image
import urllib

options = Options()
user_agent = 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/111.0.5563.146 Safari/537.36'
options = uc.ChromeOptions()
options.add_argument(
'--no-first-run --no-service-autorun --password-store=basic')
options.add_argument(f'--disable-gpu')
options.add_argument(f'--no-sandbox')
options.add_argument(f'--disable-dev-shm-usage')
options.add_argument(f'--user-agent='+str(user_agent))
CHROME_DRIVER_PATH = './chromedriver'
driver = uc.Chrome(executable_path=CHROME_DRIVER_PATH,
                    options=options, headless=False)

driver.get('https://app.farmacialabomba.com//Images/Upload/1/1/99009435.jpg')
time.sleep(5)
# Encontrar el elemento de la imagen
imagen = driver.find_element(By.XPATH,'/html/body/img')

# Extraer la URL de la imagen de la variable
src = imagen.get_attribute('src')
response = requests.get(src)
#print(response.status_code)
urllib.request.urlretrieve(src, 'image.jpg')
driver.quit()
