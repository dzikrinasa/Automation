#implicity wait adalah fungsi untuk menunggu waktu tertentu untuk menjalankan step selanjutnya
#explicity wait sama tapi untuk element tertentu

from lib2to3.pgen2.driver import Driver
from selenium import webdriver
 
driver = webdriver.Chrome()
driver.implicitly_wait(10)
driver.get("https://demoqa.com/login")
driver.get("https://demoqa.com/books")

driver.find_element_by_id("login").click()

#explicity wait sama tapi untuk element tertentu

from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.common.exceptions import TimeoutException

driver.get("https://demoqa.com/alerts")

driver.find_element_by_id("timerAlertButton").click()

try:
    WebDriverWait(driver,10).until(EC.alert_is_present())
    driver.switch_to.alert.accept()
    print("alert berhasil di pencet")

except TimeoutException:
    print("alert gagal muncul")
    pass