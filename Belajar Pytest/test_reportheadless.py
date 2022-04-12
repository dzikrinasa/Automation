import py
from selenium import webdriver
from selenium.webdriver.common.by import By
import pytest
import time


#menghilangkan warning :
#from selenium.webdriver.common.by import By
#driver.find_element(By.ID, 'some_ID')
options = webdriver.ChromeOptions()
options.add_experimental_option('excludeSwitches', ['enable-logging'])
options.headless = True
options.add_argument("--windows-size=1920,1080")

Kunci = [
    ("sdfasd","Automati0n"),    #username salah password benar
    ("ZikriQA","jfgshfd"),    #username benar password salah
    ("dfgsdfg","fgsdfg"),    #username salah password salah
]

@pytest.fixture
def setup():
    driver = webdriver.Chrome(options=options)
    driver.minimize_window()
    driver.get("https://demoqa.com/login")
    driver.implicitly_wait(10)    
    yield driver
    driver.quit()

#TESTCASE : POSITIF

@pytest.mark.positivetest
def test_login_success(setup):
    setup.find_element(By.ID, 'userName').send_keys("ZikriQA")
    setup.find_element(By.ID, 'password').send_keys("Automati0n$")
    setup.find_element(By.ID, 'login').click()
    time.sleep(3)

    mainHeader = setup.find_element(By.CLASS_NAME,"main-header").text

    assert mainHeader == "Profile"

#TESTCASE : POSITIF

@pytest.mark.negativetest
@pytest.mark.parametrize('a,b', Kunci)
def test_login_fail(setup,a,b):
    setup.find_element_by_id("userName").send_keys(a)
    setup.find_element_by_id("password").send_keys(b)
    setup.find_element_by_id("login").click()

    invalidText = setup.find_element_by_id("name").text

    assert invalidText == "Invalid username or password!"

    #Run : python -m pytest .\test_custommarker.py -v -m positivetest
    #Configurasi ditambahkan file pytest.ini di folder
    #cara run report = python -m pytest .\test_reportheadless.py -v --html=report.html