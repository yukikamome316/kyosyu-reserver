from selenium import webdriver
from selenium.webdriver.chrome.service import Service

options = webdriver.ChromeOptions()
options.add_argument('--disable-gpu');
options.add_argument('--disable-extensions');
options.add_argument('--start-maximized');
options.add_experimental_option("excludeSwitches", ['enable-automation'])

chromedriver_path = './chromedriver.exe'
service = Service(executable_path=chromedriver_path)
driver = webdriver.Chrome(service=service, options=options)
print(type(driver))
