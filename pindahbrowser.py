from selenium import webdriver 
import time

driver = webdriver.Chrome()
driver.get("https://the-internet.herokuapp.com/windows")
time.sleep(2)
driver.find_element_by_link_text("Click Here").click()
time.sleep(2)
driver.switch_to_window(driver.window_handles[0])
driver.find_element_by_link_text("Click Here").click()
time.sleep(2)
driver.switch_to_window(driver.window_handles[0])
driver.find_element_by_link_text("Click Here").click()
time.sleep(2)
driver.switch_to_window(driver.window_handles[0])
driver.find_element_by_link_text("Click Here").click()
time.sleep(2)
driver.switch_to_window(driver.window_handles[0])
