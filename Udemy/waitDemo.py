#Implicit wait
#Explicit wait
#pause test for few seconds using time class

from selenium import webdriver
from selenium.webdriver.common.by import By
import time


driver = webdriver.Chrome()
driver.get("https://rahulshettyacademy.com/seleniumPractise/#/")
driver.implicitly_wait(5)
#wait until 5 second if object is not displayed
#global wait
#1.5 second to reach next page- execution will resume in 1.5 second
#if object do not show up at all, then max time your test wait for 5 second, & show up error
driver.find_element(By.CLASS_NAME,"search-keyword").send_keys("ber")
time.sleep(5)
count = len(driver.find_elements(By.XPATH,"//div[@class='product-action']/button"))
print(count)
assert count == 3
buttons = driver.find_elements(By.XPATH,"//div[@class='product-action']/button")
for button in buttons:
    button.click()

driver.find_element(By.XPATH,'//*[@id="root"]/div/header/div/div[3]/a[4]/img').click()
driver.find_element(By.XPATH,'//*[@id="root"]/div/header/div/div[3]/div[2]/div[2]/button').click()
driver.find_element(By.CLASS_NAME,'promoCode').send_keys("rahulshettyacademy")
driver.find_element(By.CLASS_NAME,'promoBtn').click()
print(driver.find_element(By.CLASS_NAME,'promoInfo').text)