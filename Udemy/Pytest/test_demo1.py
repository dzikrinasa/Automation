"""
- any pytest file should start with test_ or end with _test
- pytest method names should start with test
- any code should be wrapped in method only
- run pytest : #Run : python -m pytest
- run more information : python -m pytest -v
- run with output visible : python -m pytest -s
- run with spesific file/method : python -m pytest test_demo1.py
- if you have same name method will replace, method name should have sense
- run only with spesific word/name of method : python -m pytest -k CreditCard -v -s
- run only with mark : python -m pytest -m smoke -v -s
- run except/skip some method/test : @pytest.mark.skip
- run test without reporting : @pytest.mark.xfail
- run prerequest order : @pytest.fixture()
- fixtures are used as setup and tear down methods for test cases - conftest.py file to generalize fixture and make it available to all test cases
- data driven and parameterization can be done with return statements in tuple format
- when you define fixture scope to class only, it will run once before class is initiated and at the end
- run report html : python -m pytest --html=report.html
"""
import pytest

@pytest.mark.smoke
def test_firstProgram():
    print("Hello")

@pytest.mark.xfail
def test_SecondGreetCreditCard():
    print("Good Morning")

def test_fixtureDemo(setup): #add argument fixture method name
        print("I will execute steps in fixtureDemo method")


def test_crossBrowser(crossBrowser):
    print(crossBrowser[1])
