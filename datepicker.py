from lib2to3.pgen2 import driver
from time import time
from selenium import webdriver
import time
import pyautogui

driver = webdriver.Chrome()
driver.implicitly_wait(10)
driver.maximize_window()
driver.get('https://jqueryui.com/datepicker/')

driver.switch_to.frame(driver.find_element_by_xpath('//*[@id="content"]/iframe'))
driver.find_element_by_id('datepicker').click()
driver.find_element_by_xpath('//*[@id="ui-datepicker-div"]/table/tbody/tr[2]/td[4]/a').click()
driver.find_element_by_id('datepicker').clear()
driver.find_element_by_id('datepicker').send_keys('11/11/2011')

driver.get('https://demoqa.com/date-picker')

driver.find_element_by_id('datePickerMonthYearInput').click()
pyautogui.press('backspace',presses=10)
time.sleep(3)
driver.find_element_by_id('datePickerMonthYearInput').send_keys('11/11/2011')
pyautogui.press('enter')