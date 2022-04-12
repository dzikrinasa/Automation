from selenium import webdriver 
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.common.exceptions import TimeoutException
import time

options = webdriver.ChromeOptions()
options.add_experimental_option('excludeSwitches', ['enable-logging'])
options.add_argument("--window-size=400,800")

driver = webdriver.Chrome(options=options)

driver.get("https://owner.smartlink.id/login") 
driver.implicitly_wait(30)
driver.find_element(By.ID, "nav-profile-tab").click()
driver.find_element(By.ID, "nav-profile-tab").click()
driver.find_element(By.ID,"input-2").send_keys("alfa.alkaaf@gmail.com")
driver.find_element(By.ID,"password-field").send_keys("citridia2014")
time.sleep(2)
driver.find_element(By.ID,"btnLoginEmail").click()
try:
    WebDriverWait(driver,10).until(EC.element_to_be_clickable((By.CLASS_NAME, 'skip-incontext')))
    print("modal dah muncul")
    time.sleep(2)
    driver.find_element(By.CLASS_NAME,"skip-incontext").click()
    driver.find_element(By.ID,"btn-secondary").click()
    print("modal dah di close")
except TimeoutException:
    print("modal gk muncul lur")
    pass

try:
    WebDriverWait(driver,30).until(EC.presence_of_element_located((By.XPATH, '//*[@id="so-title-bar"]/div/div[2]')))
    WA = driver.find_element(By.XPATH,'//*[@id="so-title-bar"]/div/div[2]').text
    assert WA ==  "Perangkat WA" 
    print("Menu WA tampil")
except TimeoutException:
    print("menu WA gk tampil")
    pass

try:
    WebDriverWait(driver,1000).until(EC.presence_of_element_located((By.XPATH, "//div[text()='Transaksi & Pembatalan '")))
    driver.find_element(By.XPATH,"//div[text()='Transaksi & Pembatalan '").click()
except TimeoutException:
    print("menu gk tampil c")
    pass


# driver.find_element(By.XPATH,'//*[@id="view-screen"]/div/div/div[1]/div[2]/div[2]/div/div[1]/div/div/div').click()
# driver.find_element(By.XPATH,'//*[@id="view-screen"]/div/div/div/div[1]/div[2]/div[2]/div[2]/div[1]/div/div/div[2]/div[2]').click()
# driver.find_element(By.XPATH,'//*[@id="view-screen"]/div/div/div/div[1]/div[2]/div[2]/div[2]/div[1]/div/div/div[2]/div[3]/button[1]').click()
# driver.find_element(By.XPATH,'//*[@id="modal574154"]/div/div/div[2]/div/form/div/div/div/input').send_keys("okay")
# driver.find_element(By.XPATH,'//*[@id="574154"]/span').click()




