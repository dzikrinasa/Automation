import py
from selenium import webdriver
import pytest

Kunci = [
    ("sdfasd","Automati0n"),    #username salah password benar
    ("ZikriQA","jfgshfd"),    #username benar password salah
    ("dfgsdfg","fgsdfg"),    #username salah password salah
    ("ZikriQA","Automati0n$"),    #username benar password benar
]

driver = webdriver.Chrome()
driver.implicitly_wait(10)

@pytest.mark.parametrize('a,b', Kunci)
def test_login(a,b):
    driver.get("https://demoqa.com/login")
    driver.find_element_by_id("userName").send_keys(a)
    driver.find_element_by_id("password").send_keys(b)
    driver.find_element_by_id("login").click()

    invalidText = driver.find_element_by_id("name").text

    assert invalidText == "Invalid username or password!"