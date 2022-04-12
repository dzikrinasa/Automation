
from lib2to3.pgen2 import driver
from selenium import webdriver
from selenium.webdriver.support.select import Select
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions

options = webdriver.ChromeOptions()
options.add_experimental_option('excludeSwitches', ['enable-logging'])

driver = webdriver.Chrome(options=options)

driver.get("https://rahulshettyacademy.com/angularpractice/")
driver.find_element(By.LINK_TEXT,"Shop").click()
products = driver.find_elements(By.XPATH,"//div[@class='card h-100']") #whole card

for product in products:
    productName = product.find_element(By.XPATH,"div/h4/a").text #card text path, search from spesific path
    if productName == "Blackberry":
        #add card to cart
        product.find_element(By.XPATH,"div/button").click() #path to button of card

driver.find_element(By.XPATH,"//a[contains(@class,'nav-link btn')]").click()
driver.find_element(By.CLASS_NAME,"btn-success").click()

driver.find_element(By.ID,"country").send_keys("ind")
wait = WebDriverWait(driver, 10)
wait.until(expected_conditions.presence_of_element_located((By.LINK_TEXT, "Indonesia")))#Expected Condition
driver.find_element(By.LINK_TEXT,"Indonesia").click()
driver.find_element(By.CLASS_NAME,"checkbox-primary").click()
driver.find_element(By.CSS_SELECTOR,"[type='submit']").click() #css selector using type
successText = driver.find_element(By.CLASS_NAME,"alert-success").text

assert "Success! Thank you!" in successText

#screenshot
driver.get_screenshot_as_file("screen.png")