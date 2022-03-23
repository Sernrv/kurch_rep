# b = 5
# c = 6
# match b, c:
#     case 1, 2:
#         print('Yes')
#     case _:
#         print('No')
#
# l = [a for a in range(1, 8)]
# print(l)
# for m in l:
#     print(m)


# import timeit as ti
# import sys
#
# t1 = ti.default_timer()
# cities = ['Москва', 'Астрахань', 'Казань', 'Санкт_Петербург']
# leng = []
# for w in cities:
#     leng.append(len(w))
# print(leng)
# t2 = ti.default_timer()
# print(sys.getsizeof(leng))
# print(t2 - t1)

import timeit as ti
import sys

t1 = ti.default_timer()
cities = ['Москва', 'Астрахань', 'Казань', 'Санкт_Петербург']
b = map(len, cities)
a = list(b)
print(a)
t2 = ti.default_timer()
print(sys.getsizeof(b))
print(sys.getsizeof(a))
print(t2 - t1)
