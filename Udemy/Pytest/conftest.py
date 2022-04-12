import pytest

#@pytest.fixture()
@pytest.fixture(scope="class")
def setup():
    print("I will be executing this first")
    yield #hold & run after test done/last
    print(" I will executed last")

@pytest.fixture()
def dataLoad():
    print("User Profile data is being created")
    return ["John", "Doe", "jhondoe.com"]

@pytest.fixture(params=[("chrome","John","Doe"), ("Firefox","Boboy"), ("IE","SS")])
def crossBrowser(request):
    return request.param
