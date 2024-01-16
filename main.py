import os
from dotenv import load_dotenv

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# .envファイルの読み込み
load_dotenv()

options = webdriver.ChromeOptions()
options.add_argument('--disable-gpu');
options.add_argument('--disable-extensions');
options.add_argument('--start-maximized');
options.add_experimental_option("excludeSwitches", ['enable-automation'])

chromedriver_path = os.getenv('CHROMEDRIVER_PATH')
obicnet_url = os.getenv('OBICNET_URL')
student_id = os.getenv('STUDENT_ID')
password = os.getenv('PASSWORD')

service = Service(executable_path=chromedriver_path)
driver = webdriver.Chrome(service=service, options=options)

driver.set_page_load_timeout(30)
# driver.implicitly_wait(5)

driver.get(obicnet_url)

# ログインページへ
e_login_page_button = driver.find_element(By.ID, 'lnkToLogin')
e_login_page_button.click()

wait = WebDriverWait(driver, 10)

e_iframe = wait.until(EC.presence_of_element_located((By.ID, 'frameMenu')))
driver.switch_to.frame(e_iframe)

# ログイン情報の入力
e_kyosyusei_id = wait.until(EC.presence_of_element_located((By.ID, 'txtKyoushuuseiNO')))
e_password = driver.find_element(By.ID, 'txtPassword')

e_kyosyusei_id.send_keys(student_id)
e_password.send_keys(password)

e_login_button = driver.find_element(By.ID, 'btnAuthentication')
e_login_button.click()
