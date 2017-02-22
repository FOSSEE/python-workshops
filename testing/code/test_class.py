
class TestSomething(object):
    def test_something_has_hello(self):
        x = 'hello1'
        y = 'hello world'
        assert x in y

    def test_something_else(self):
        a = [1, 2, 3]
        b = {1, 2, 3}
        assert a == b
