from calculator import square

#pip install pytest

# no main function, no try, no exceptions, etc....
# run pytest test_calc.py instead.

def test_square():
    assert square(2) == 4
    assert square(3) == 9
    assert square(-2) == 4
    assert square(-3) == 9
    assert square(0) == 0


#OUTPUT:
'''
==================================================================== test session starts =====================================================================
platform linux -- Python 3.10.12, pytest-7.4.3, pluggy-1.3.0
rootdir: /home/justin/github/cs50p/Week 5/Calculator
collected 1 item                                                                                                                                             

test_calc.py F    
========================================================================== FAILURES ==========================================================================
________________________________________________________________________ test_square _________________________________________________________________________

    def test_square():
        assert square(2) == 4
>       assert square(3) == 9
E       assert 6 == 9
E        +  where 6 = square(3)

test_calc.py:10: AssertionError
================================================================== short test summary info ===================================================================
FAILED test_calc.py::test_square - assert 6 == 9
===================================================================== 1 failed in 0.03s ======================================================================
'''

#Good pyest below:
'''
pytest test_calc.py
==================================================================== test session starts =====================================================================
platform linux -- Python 3.10.12, pytest-7.4.3, pluggy-1.3.0
rootdir: /home/justin/github/cs50p/Week 5/Calculator
collected 1 item                                                                                                                                             

test_calc.py .                                                                                                                                         [100%]

===================================================================== 1 passed in 0.01s ======================================================================
'''