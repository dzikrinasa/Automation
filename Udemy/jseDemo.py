#Js DOM can access any elements on web page just like how selenium does
# selenium have a method to execute javascript code in it

from ast import arguments
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver import ActionChains

options = webdriver.ChromeOptions()
options.add_experimental_option('excludeSwitches', ['enable-logging'])

driver = webdriver.Chrome(options=options)

driver.get("https://rahulshettyacademy.com/angularpractice/")

driver.find_element(By.NAME,"name").send_keys("hello")
print(driver.find_element(By.NAME,"name").text)
print(driver.find_element(By.NAME,"name").get_attribute("value"))
print(driver.execute_script('return document.getElementsByName("name")[0].value')) #javascript run

shop = driver.find_element(By.LINK_TEXT,"Shop")
driver.execute_script('arguments[0].click()',shop)
#scroll by javascript
driver.execute_script("window.scrollTo(0,document.body.scrollHeight);")
