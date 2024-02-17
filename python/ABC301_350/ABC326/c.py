n, m = map(int, input().split())
a = [int(a_i) for a_i in input().split()]

a.sort()

def is_ok(i, key):
    return a[i] >= key


def binary_search(key):
    ng = -1
    ok = n

    while abs(ok - ng) > 1:
        mid = (ok + ng) // 2
        if is_ok(mid, key):
            ok = mid
        else:
            ng = mid
    return ok


# o(nlogn
res = -1
for i in range(len(a)):
    ai = a[i]
    j = binary_search(ai + m)
    if res < (j - i):
        res = j - i
print(res)
