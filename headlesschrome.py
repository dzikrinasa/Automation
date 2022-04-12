from selenium import webdriver

options = webdriver.ChromeOptions()
options.headless = True

driver = webdriver.Chrome(options=options)
driver.get("https://demoqa.com")
print(driver.title)