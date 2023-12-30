from hello import hello

'''
def test_hello():
    assert hello("Justin") == "hello, Justin"
    assert hello() == "hello, world"
'''

def test_default():
    assert hello() == "hello, world"

def test_argument():
    assert hello("Justin") == "hello, Justin"