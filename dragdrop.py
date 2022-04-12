import imp
from lib2to3.pgen2 import driver
from xml.dom.minidom import Element
from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains

driver = webdriver.Chrome()

driver.get("https://demoqa.com/droppable")
driver.maximize_window()
driver.implicitly_wait(10)

drag = driver.find_element_by_id('draggable')
drop = driver.find_element_by_id('droppable')

action = ActionChains(driver)

action.drag_and_drop(drag, drop).perform()