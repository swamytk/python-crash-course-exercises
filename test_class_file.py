import pytest
from class_file import HomeClass

@pytest.fixture
def my_home():  # This function name should be same as return data
    # The below should pass
    my_home = HomeClass(800, 'Egmore', 7000)
    # The below all should fail
    #my_home = HomeClass(-300, 'Egmore', 7000)
    #my_home = HomeClass(700, 'Egmore', 0)
    #my_home = HomeClass(-40, 'Egmore', -30)

    return my_home

def test_sqft(my_home):
    assert my_home.sqft > 0

def test_price(my_home):
    assert my_home.rate > 0

# Test this module by running just 'pytest' command in shell.