from selenium import webdriver
import pytest

driver = webdriver.Chrome()
driver.minimize_window()
def test_bukaGoogel():
    driver.get("https://www.google.com")
    Title = driver.title
    
    assert Title == "Google"

def test_bukaFB():
    driver.get("https://www.facebook.com")
    Title = driver.title

    assert Title == "Facebook"