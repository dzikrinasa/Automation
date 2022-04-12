
import time
from selenium import webdriver

driver = webdriver.Chrome()

driver.get("https://rahulshettyacademy.com/dropdownsPractise/")
name = driver.find_element_by_id("autosuggest")
name.send_keys("ind")
time.sleep(2)
countries = driver.find_elements_by_class_name("ui-menu-item")
print(len(countries))
for country in countries:
    if country.text == "Indonesia":
        country.click()
        break
print(name.text)
assert name.get_attribute('value') == "Indonesia"
print(name.get_attribute('value'))