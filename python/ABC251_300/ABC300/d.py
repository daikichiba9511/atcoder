n = int(input())


def eratosthenes(n):
    isprime = [True] * (n + 1)
    isprime[0] = False
    isprime[1] = False

    for p in range(2, n + 1):
        # skip if p is not prime
        if not isprime[p]:
            continue

        # remove multiples of p
        for q in range(2 * p, n + 1, p):
            isprime[q] = False

    return [p for p in range(n + 1) if isprime[p]]


p = eratosthenes(n if n < 3 * 10**5 else 3 * 10**5)
pb = len(p)  # <= 25997 = O(10**4)

res = 0
# i: 左端から
# j: iの一つとなり
# k: 右端から
# O(pb^2) = O(10**8)かつwhileつかってるからたぶん間に合わない
# for i in range(pb):
#     k = pb - 1
#     j = i + 1
#     while j < k and j < pb:
#         while j < k:
#             v = p[i] * p[i] * p[j]
#             if v > n:
#                 # この時点で値を越えたら右端を一つ狭めて抜ける
#                 k -= 1
#                 continue
#             v *= p[k]
#             if v > n:
#                 k -= 1
#                 continue
#             v *= p[k]
#             if v > n:
#                 k -= 1
#                 continue
#             break
#         res += k - j
#         j += 1
#         # if res == 3:
#         #     print(p[i], p[j], p[k], res)
#         #     exit()
#         # print(p[i], p[j], p[k], res)
# print(res)

# e.g.
# 2 3 5 7 11 13 17 19 23 29 31 37 41 43 47
# i j                    k*           <- k
#     <----------------->
#     ここは選べるからk-jをresに足す
res = 0
for i in range(pb):
    # 隣り合ってる素数の積が越えてたらそれより右側は見なくていい
    if p[i] ** 2 * p[i + 1] * p[i + 2] ** 2 > n:
        break
    for j in range(i + 1, pb):
        # あるiと隣り合ってるjとj+1の積が越えてたらjより右側は見なくていい(ここで計算した積よりも大きくなるから)
        if p[i] ** 2 * p[j] * p[j + 1] ** 2 > n:
            break
        for k in range(j + 1, pb):
            v = p[i] * p[i] * p[j]
            if v > n:
                break
            v *= p[k]
            if v > n:
                break
            v *= p[k]
            if v > n:
                break
            res += 1
print(res)
