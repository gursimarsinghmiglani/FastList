from fastlist import FastList
from random import randint
from timeit import timeit


def f(xs):
    n = 500000
    m = 1000
    for _ in range(n):
        i = randint(0, len(xs))
        xs.insert(i, randint(0, m))
    for _ in range(n):
        i = randint(0, len(xs) - 1)
        xs[i] = randint(0, m)
    for _ in range(n):
        i = randint(0, len(xs) - 1)
        del xs[i]


lst = []
fastlst = FastList()
print("Time taken by ordinary list: {} seconds".format(timeit(lambda: f(lst), number=1)))
print("Time taken by FastList: {} seconds".format(timeit(lambda: f(fastlst), number=1)))
