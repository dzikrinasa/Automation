from selenium import webdriver
from selenium.webdriver.support.ui import Select

driver = webdriver.Chrome()
driver.get("https://rahulshettyacademy.com/angularpractice/")

driver.find_element_by_name("name").send_keys("Jhon") #name
driver.find_element_by_css_selector("input[name='name']").send_keys(" Doe") #css selector
driver.find_element_by_name("email").send_keys("fuck@gmail.com") #name
driver.find_element_by_id("exampleCheck1").click() #ID
#select class provide the methods to handle the options in dropdown
dropdown = Select(driver.find_element_by_id("exampleFormControlSelect1"))
dropdown.select_by_visible_text("Female")
#dropdown.select_by_index(0)
driver.find_element_by_xpath("//body/app-root[1]/form-comp[1]/div[1]/form[1]/input[1]").click() #Xpath
massage = driver.find_element_by_class_name("alert-success").text #class divine by space
assert "success" in massage


#plugin ChroPath for copy css selector & xpath
#path to child using /
#path to parent using ::