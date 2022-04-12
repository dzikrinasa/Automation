from selenium import webdriver
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.common.by import By
import time
from lib2to3.pgen2 import driver

driver = webdriver.Chrome()

driver.get("https:tees.co.id/")

for i in range (2):
    driver.get("https:tees.co.id/")
    
    try:
        WebDriverWait(driver,10).until(EC.visibility_of_all_elements_located((By.XPATH, '/html/body/div[1]')))
        print("modal dah muncul")
        driver.find_element_by_class_name("btn-modal-close").click()
        print("modal dah di close")
    
    except TimeoutException:
        print("modal gk muncul lur")
        pass

time.sleep(3)