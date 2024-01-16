import os
from dotenv import load_dotenv

from selenium import webdriver
from selenium.webdriver.chrome.service import Service

# .envファイルの読み込み
load_dotenv()

options = webdriver.ChromeOptions()
options.add_argument('--disable-gpu');
options.add_argument('--disable-extensions');
options.add_argument('--start-maximized');
options.add_experimental_option("excludeSwitches", ['enable-automation'])

chromedriver_path = os.getenv('CHROMEDRIVER_PATH')
obicnet_url = os.getenv('OBICNET_URL')

service = Service(executable_path=chromedriver_path)
driver = webdriver.Chrome(service=service, options=options)
driver.get(obicnet_url)


