from function_file import arithmetic

def test_arithmetic1():
    sum = arithmetic(10,20,5)
    assert sum == 25
    # The below wrong expected result should cause AssertionError
    #assert sum == 15

# Test this module by running just 'pytest' command in shell.
