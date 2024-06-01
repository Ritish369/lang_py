# Its purpose to exist in life is to test the specif functionality of 
# the file, func_calc.py
from func_calc import square

# For the test_str(), additionally import the pytest library
import pytest

#def main():
#    test_square()

"""
def test_square():
    
    if square(2) != 4:
        print("2 squared was not 4")
    if square(3) != 9:
        print("3 squared was not 9")
    
    # Alternate and easy way to test i.e., just by flipping the logic
    # But not much user-friendly

    try:
        assert square(2) == 4
    except AssertionError:
        print("2 squared was not 4")
    try:
        assert square(3) == 9
    except AssertionError:
        print("3 squared was not 9")
    try:
        assert square(-2) == 4
    except AssertionError:
        print("-2 squared was not 4")
    try:
        assert square(-3) == 9
    except AssertionError:
        print("-3 squared was not 9")
    try:
        assert square(0) == 0
    except AssertionError:
        print("0 squared was not 0")
    
    # Using pytest to distill the testing process i.e., reducing the LOCs
    # and automate testing
    # Its also pretty user-friendly as testing frameworks go
    
    assert square(2) == 4
    assert square(3) == 9
    assert square(-2) == 4
    assert square(-3) == 9
    assert square(0) == 0
    
    # Alternate way to write the same thing
    for i in [-2, -3, 0, 2, 3]:
        assert square(i) == i * i

    # Here comes the pytest into play i.e., to handle the try, excepts
    # and other printing stuff by automating all these and informs for 
    # any of the test failing i.e., all standardizations of testing
    
    # Also, pytest, in some sense, gives you just clues for what
    # must be wrong
   """
   
   # Now, to get more clues for specifically which test are failing, it 
   # is always better to divide the big single test into multiple 
   # categorised(can be done in any type) test functions.
   # This is done as follows:
def test_positive():
    assert square(2) == 4
    assert square(3) == 9
    
def test_negative():
    assert square(-2) == 4
    assert square(-3) == 9
    
def test_zero():
    assert square(0) == 0
    
def test_str():
    # raises fn of pytest allows to express that the coder expects 
    # an exception to be raised
    # In parentheses is the the type of error expected
    with pytest.raises(TypeError):
        # Here comes, when is it expected to be raised
        square("cat")
    
#if __name__ == "__main__":
#    main()