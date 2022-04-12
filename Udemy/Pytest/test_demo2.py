
import pytest


@pytest.mark.smoke
#@pytest.mark.skip
def test_firstProgram():
    msg = "Hello"
    assert msg == "Hi", "Test failed because strings do not match"

def test_SecondCreditCard():
    a = 4
    b = 6
    assert a + 2 == b , "addition do not match"

@pytest.fixture()
def setup():
    print("I will be executing this first")

def test_fixtureDemo(setup): #add argument fixture method name
    print("I will execute steps in fixtureDemo method")
