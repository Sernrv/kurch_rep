#%%
a = float(input())
try:
    b = 7 / a
except:
    print('Все неправильно!')
finally:
    print('В любом случае неправильно...')
