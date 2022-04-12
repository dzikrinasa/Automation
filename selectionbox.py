from lib2to3.pgen2 import driver
from selenium import webdriver
from selenium.webdriver.support.ui import Select
import pyautogui

driver = webdriver.Chrome()
driver.maximize_window()
driver.implicitly_wait(10)

driver.get('https://demoqa.com/select-menu')

#oldSelect
pilih = Select(driver.find_element_by_id('oldSelectMenu'))
pilih.select_by_visible_text('Yellow')
pilih.select_by_value('10')
#selectone
driver.find_element_by_id('selectOne').click()
pyautogui.typewrite('Prof.')
pyautogui.press('enter')
#multiselect
driver.find_element_by_xpath('//*[@id="selectMenuContainer"]/div[7]/div/div/div').click()
pyautogui.typewrite('Blue')
pyautogui.press('enter')
pyautogui.typewrite('Red')
pyautogui.press('enter')

