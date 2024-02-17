import random
import time

import numpy as np

num_iter = 3000
n = 10_000


def timeit(n, func):
    duratios = []
    for _ in range(n):
        start = time.time()
        func()
        duration = time.time() - start
        duratios.append(duration)

    print(f"average: {sum(duratios) / n}")
    print(f"min: {min(duratios)}")
    print(f"max: {max(duratios)}")


def py_list_insert_slice():
    a = list(range(n)) + [0]

    for _ in range(num_iter):
        l = random.randint(0, n)
        r = random.randint(l, n + 1)
        a[l:r] = a[l:r][::-1]


def py_list_new_create():
    a = list(range(n)) + [0]

    for _ in range(num_iter):
        l = random.randint(0, n)
        r = random.randint(l, n + 1)
        a = a[:l] + a[l:r][::-1] + a[r:]


def numpy_insert_slice():
    a = np.arange(n)
    a[-1] = 0

    for _ in range(num_iter):
        l = random.randint(0, n)
        r = random.randint(l, n + 1)
        a[l:r] = a[l:r][::-1]


def numpy_new_create():
    a = np.arange(n)
    a[-1] = 0

    for _ in range(num_iter):
        l = random.randint(0, n)
        r = random.randint(l, n + 1)
        a = np.concatenate([a[:l], a[l:r][::-1], a[r:]])


if __name__ == "__main__":
    print("\n#### py_list_insert_slice\n")
    timeit(100, py_list_insert_slice)

    print("\n#### py_list_new_create\n")
    timeit(100, py_list_new_create)

    print("\n#### numpy_insert_slice\n")
    timeit(100, numpy_insert_slice)

    print("\n#### numpy_new_create\n")
    timeit(100, numpy_new_create)
