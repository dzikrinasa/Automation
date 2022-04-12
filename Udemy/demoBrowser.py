from selenium import webdriver
#browser exposes an executable file
#trhough selenium test we neet to invoke the executable file which will  then invoke actual browser
driver = webdriver.Chrome(executable_path="C:\\chromedriver.exe")
driver.maximize_window()
driver.get("https://rahulshettyacademy.com/") #get method to hit url on browser

print(driver.title)
print(driver.current_url)
driver.get("https://rahulshettyacademy.com/AutomationPractice/")
driver.minimize_window()
driver.back()
driver.refresh()
driver.close()