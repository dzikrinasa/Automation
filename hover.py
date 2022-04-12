from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains

driver = webdriver.Chrome()

driver.get("https://demoqa.com/menu")
driver.maximize_window()
driver.implicitly_wait(10)

#cara1 

menu = driver.find_element_by_link_text("Main Item 2")

Hover = ActionChains(driver).move_to_element(menu)

Hover.perform()

#cara2

ActionChains(driver).move_to_element((driver.find_element_by_link_text('Main Item 2'))).perform()