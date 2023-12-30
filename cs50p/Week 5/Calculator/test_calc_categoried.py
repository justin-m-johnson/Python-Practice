import pytest
from calculator import square

#pip install pytest

# no main function, no try, no exceptions, etc....
# run pytest test_calc.py instead.
#Here we have defined three functions to test. pytest will test all three instead of stopping at the first error in a long stack...

def test_postive():
    assert square(2) == 4
    assert square(3) == 9

def test_negative():
    assert square(-2) == 4
    assert square(-3) == 9

def test_zero():
    assert square(0) == 0

#OUTPUT:
'''
pytest test_calc_categoried.py
==================================================================== test session starts =====================================================================
platform linux -- Python 3.10.12, pytest-7.4.3, pluggy-1.3.0
rootdir: /home/justin/github/cs50p/Week 5/Calculator
collected 3 items                                                                                                                                            

test_calc_categoried.py FF.                                                                                                                            [100%]

========================================================================== FAILURES ==========================================================================
________________________________________________________________________ test_postive ________________________________________________________________________

    def test_postive():
        assert square(2) == 4
>       assert square(3) == 9
E       assert 6 == 9
E        +  where 6 = square(3)

test_calc_categoried.py:11: AssertionError
_______________________________________________________________________ test_negative ________________________________________________________________________

    def test_negative():
>       assert square(-2) == 4
E       assert -4 == 4
E        +  where -4 = square(-2)

test_calc_categoried.py:14: AssertionError
================================================================== short test summary info ===================================================================
FAILED test_calc_categoried.py::test_postive - assert 6 == 9
FAILED test_calc_categoried.py::test_negative - assert -4 == 4
================================================================ 2 failed, 1 passed in 0.03s =================================================================
'''

def test_str():
    with pytest.raises(TypeError):
        square("cat")