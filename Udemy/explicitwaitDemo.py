#Implicit wait
#Explicit wait - target only specific element
#pause test for few seconds using time class

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions
import time

def compare(a, b):
    found = False
    for x, y in zip(a, b):
        if x in y: found = True
        else: found = False
    return found

options = webdriver.ChromeOptions()
options.add_experimental_option('excludeSwitches', ['enable-logging'])

list = []
list2 = []
driver = webdriver.Chrome(options=options)
driver.get("https://rahulshettyacademy.com/seleniumPractise/#/")
driver.find_element(By.CLASS_NAME,"search-keyword").send_keys("berghgjh")
time.sleep(5)
key = driver.find_element(By.CLASS_NAME,"search-keyword").get_attribute("value")
count = len(driver.find_elements(By.XPATH,"//div[@class='product-action']/button"))
print(count)
assert count == 3
buttons = driver.find_elements(By.XPATH,"//div[@class='product-action']/button")
for button in buttons:
    list.append(button.find_element(By.XPATH,"parent::div/parent::div/h4").text) #root path to text
    button.click()
print(list)
keyword = []
keyword = [key] * count
print(keyword)

# if len(set(keyword).intersection(list)) != 0:
#     print("Found")
# else:
#     print("Not Found")


assert compare(keyword, list)

# assert keyword in list
# print("search match")

driver.find_element(By.XPATH,'//*[@id="root"]/div/header/div/div[3]/a[4]/img').click()
driver.find_element(By.XPATH,'//*[@id="root"]/div/header/div/div[3]/div[2]/div[2]/button').click()
#explicit wait
wait = WebDriverWait(driver, 10)
wait.until(expected_conditions.presence_of_element_located((By.CLASS_NAME, "promoCode")))#Expected Condition

veggies = driver.find_elements(By.CLASS_NAME,"product-name")
for veg in veggies:
    list2.append(veg.text)
print(list2)
assert list == list2
originalAmount = driver.find_element(By.CLASS_NAME, 'discountAmt').text
driver.find_element(By.CLASS_NAME,'promoCode').send_keys("rahulshettyacademy")
driver.find_element(By.CLASS_NAME,'promoBtn').click()

wait.until(expected_conditions.presence_of_element_located((By.CSS_SELECTOR, "span.promoInfo")))#Expected Condition#
#wait.until(expected_conditions.pre(By.CLASS_NAME,'promoInfo'))
print(driver.find_element(By.CLASS_NAME,'promoInfo').text)

discountAmount = driver.find_element(By.CLASS_NAME, 'discountAmt').text

assert float(discountAmount) < int(originalAmount)

amounts = driver.find_elements(By.XPATH,'//tr/td[5]/p') #table path amount
sum = 0
for amount in amounts:
    sum = sum + int(amount.text) #32+48+60

print(sum)

totalAmount = int(driver.find_element(By.CLASS_NAME,'totAmt').text)
assert sum == totalAmount