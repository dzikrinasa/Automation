from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions
import time

options = webdriver.ChromeOptions()
options.add_experimental_option('excludeSwitches', ['enable-logging'])

driver = webdriver.Chrome(options=options)

driver.get("https://the-internet.herokuapp.com/windows")

driver.find_element(By.LINK_TEXT,"Click Here").click()
childwindow = driver.window_handles[1] # tab number id
#("parentid","childid")
driver.switch_to.window(childwindow)
print(driver.find_element(By.TAG_NAME,"h3").text)
driver.switch_to.window(driver.window_handles[0])
assert "Opening a new window" == driver.find_element(By.TAG_NAME,"h3").text