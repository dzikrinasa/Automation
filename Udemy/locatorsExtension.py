from lib2to3.pgen2 import driver
from selenium import webdriver
import time
driver = webdriver.Chrome()
driver.get("https://login.salesforce.com/")
driver.find_element_by_css_selector("#username").send_keys("Howard")
driver.find_element_by_css_selector(".password").send_keys("shetty")
driver.find_element_by_css_selector(".password").clear()
driver.find_element_by_link_text("Forgot Your Password?").click()
driver.find_element_by_xpath('//*[@id="forgotPassForm"]/div[1]/input[3]').click()
#print(driver.find_element_by_xpath('//form*[@name="login"]/div[1]/label').text)
#print(driver.find_elements_by_css_selector("form[name='login'] label:nth-child(3)").text)