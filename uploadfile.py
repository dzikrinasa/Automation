from lib2to3.pgen2 import driver
from time import time
from selenium import webdriver
import pyautogui
import time 
driver = webdriver.Chrome()

driver.get("https://demoqa.com/upload-download")

driver.find_element_by_id("uploadFile").send_keys("C:/Users/citri/OneDrive/Documents/Note.txt")

driver.get("https://gofile.io/uploadFiles")
driver.implicitly_wait(10)
driver.find_element_by_xpath('//*[@id="rowUploadButton"]/div/div/div/div/div/div[1]/div/button').click()

time.sleep(3)

pyautogui.write(r"C:\Users\citri\OneDrive\Documents\Note.txt")
pyautogui.press("enter")