from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver import ActionChains

options = webdriver.ChromeOptions()
options.add_experimental_option('excludeSwitches', ['enable-logging'])

driver = webdriver.Chrome(options=options)

driver.get("https://rahulshettyacademy.com/AutomationPractice/")
action = ActionChains(driver)


assert driver.find_element(By.ID,"displayed-text").is_displayed()

driver.find_element(By.ID,"hide-textbox").click()

assert not driver.find_element(By.ID,"displayed-text").is_displayed() #Assert False


hover = driver.find_element(By.ID,"mousehover")
action.move_to_element(hover).perform()
top = driver.find_element(By.LINK_TEXT,"Top")
reload = driver.find_element(By.LINK_TEXT,"Reload")
action.move_to_element(reload).click().perform()


driver.get("https://chercher.tech/practice/practice-pop-ups-selenium-webdriver")

action.context_click(driver.find_element(By.ID,"double-click")).perform() #rigth click
action.double_click(driver.find_element(By.ID,"double-click")).perform()


alert = driver.switch_to.alert
assert alert.text == "You double clicked me!!!, You got to be kidding me"
alert.accept()


print("All done")