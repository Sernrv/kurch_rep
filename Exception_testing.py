# %% Finally construction
a = float(input())
try:
    b = 7 / a
except ZeroDivisionError:
    print('Все неправильно!')
finally:
    print('В любом случае неправильно...')


# %% Raise construction
class TestException(Exception):
    """Special testing exception class"""

    def __init__(self, *args):
        self.message = args[0] if args else 'with no explanation'

    def __str__(self):
        return f'Error {self.message}'


a = float(input())
b = 5 / a
if a == 1:
    raise TestException('One division exception')


# %% Class inheritance
class GeneralTestException(Exception):
    """General testing exception class"""

    def __init__(self, *args):
        self.message = 'This is general error message'

    def __str__(self):
        return self.message


class TestException(GeneralTestException):
    """Test exception class"""

    def __init__(self, *args):
        self.message = 'this is test error message'

    def __str__(self):
        return self.message


class TestClass:
    """Test class"""

    def test_method(self):
        if True:
            raise TestException


test = TestClass.test_method('1574484684')
