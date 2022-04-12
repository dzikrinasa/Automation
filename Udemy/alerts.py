
from time import time
from selenium import webdriver

validateText = "Coba alert"
driver = webdriver.Chrome()
driver.get("https://rahulshettyacademy.com/AutomationPractice")

driver.find_element_by_id("name").send_keys(validateText)
driver.find_element_by_id("alertbtn").click()
alert = driver.switch_to.alert
alertText = alert.text
assert validateText in alertText
alert.accept()
time.sleep(3)

driver.find_element_by_id("confirmbtn").click()
confirm = driver.switch_to.alert.dissmis()
confirm.dismiss()