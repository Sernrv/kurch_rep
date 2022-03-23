# %%
a = [b*2 for b in range(7)]
print(a)        # 1-й
a.insert(5, 6)     # 2-й
print(a)    # 2-й
print('6:', a.count(6))     # 3-й
a.pop(5)
print(a)    # 4-й
c = [1, 1, 1, 1, 1, 2]
a.extend(c)
print(a)    # 5-й
a.remove(2)
print(a)    # 6-й
a.reverse()
print(a)    # 7-й
