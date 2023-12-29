from calculator import square

def main():
    test_square()

def test_square():
    try:
        assert square(2) == 4
    except AssertionError:
        print("2 Square was not 4")
    try:
        assert square(3) == 9
    except AssertionError:
        print("3 square is not 9")
    ### AssertionError
    ### I could write 30 lines of code to test 2. Dont... Download pytest... See test_calc.py

'''
Use assert instead
    if square(2) != 4:
        print("2 square was not 4")
    if square(3) != 9:
        print("3 square was not 9")
'''

if __name__ == "__main__":
    main()