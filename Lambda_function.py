# syntax -- lambda parameters:expression
from functools import reduce

s = lambda n: n * n
print(s(2))

s1 = lambda n: 2 * n
print(s1(100))

s2 = lambda a, b: a + b
print(s2(2, 3))

# filter(function,sequence) function

l = [5, 10, 15, 20, 25, 30, 35, 40, 45, 50]


def isEven(n):
    if n % 2 == 0:
        return True


def isOdd(n):
    if n % 2 != 0:
        return True


l2 = list(filter(isEven, l))
print(l)
print(l2)
l3 = list(filter(isOdd, l))
print(l3)

# Using lambda
l4 = list(filter(lambda x: x % 2 == 0, l))
print(l4)
l5 = list(filter(lambda x: x % 2 != 0, l))
print(l5)

# map(fun,seq) function
l6 = list(map(lambda x: 2 * x, l))
print(l6)
l7 = list(map(lambda x: x * x, l))
print(l7)

# reduce() function
res = reduce(lambda a, b: a + b, l)
print(res)
res1 = reduce(lambda a, b: a * b, l)
print(res1)
