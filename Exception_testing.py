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
    pass


a = float(input())
b = 5 / a
if a == 1:
    raise TestException('One division exception')
