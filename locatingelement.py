from selenium import webdriver 
from selenium.webdriver.common.by import By
import time

driver = webdriver.Chrome()

driver.get("https://the-internet.herokuapp.com/login") 
time.sleep(2)
driver.find_element_by_id("username").send_keys("uno")
time.sleep(2)
driver.find_element_by_name("password").send_keys("123456")
time.sleep(2)
driver.find_element_by_link_text("Elemental Selenium").click()

#h2 = driver.find_elements_by_tag_name("h2")
#print(h2)

#link = driver.find_elements_by_tag_name("a")
#print(len(link))

#driver.find_element_by_class_name("radius").click()
time.sleep(2)
#driver.find_element_by_css_selector("button.radius").click()
driver.find_element_by_css_selector("#login > button").click()

driver.get("https://the-internet.herokuapp.com/add_remove_elements/")
driver.find_element_by_css_selector("#content > div > button").click()
driver.find_element_by_xpath('//*[@id="content"]/div/button').click()
driver.find_element(By.XPATH,'//*[@id="content"]/div/button').click()