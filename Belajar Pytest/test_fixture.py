import py
from selenium import webdriver
import pytest
import time

Kunci = [
    ("sdfasd","Automati0n"),    #username salah password benar
    ("ZikriQA","jfgshfd"),    #username benar password salah
    ("dfgsdfg","fgsdfg"),    #username salah password salah
]

@pytest.fixture
def setup():
    driver = webdriver.Chrome()
    driver.minimize_window()
    driver.get("https://demoqa.com/login")
    driver.implicitly_wait(10)    
    yield driver
    driver.quit()


def test_login_success(setup):
    setup.find_element_by_id("userName").send_keys("ZikriQA")
    setup.find_element_by_id("password").send_keys("Automati0n$")
    setup.find_element_by_id("login").click()
    time.sleep(3)

    mainHeader = setup.find_element_by_class_name("main-header").text

    assert mainHeader == "Profile"

@pytest.mark.parametrize('a,b', Kunci)
def test_login_fail(setup,a,b):
    setup.find_element_by_id("userName").send_keys(a)
    setup.find_element_by_id("password").send_keys(b)
    setup.find_element_by_id("login").click()

    invalidText = setup.find_element_by_id("name").text

    assert invalidText == "Invalid username or password!"