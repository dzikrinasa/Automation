from selenium import webdriver
import time

driver = webdriver.Chrome()

#driver.get("https://demoqa.com/alerts")
#time.sleep(2)

#driver.find_element_by_id("alertButton").click()
#time.sleep(2)
#driver.switch_to.alert.accept()
#time.sleep(2)
driver.get("https://demoqa.com/alerts")
time.sleep(2)
#driver.find_element_by_id("promtButton").click()
driver.find_element_by_xpath('//*[@id="promtButton"]').click()
time.sleep(2)
driver.switch_to.alert.send_keys("Inputan Test")
driver.switch_to.alert.accept()