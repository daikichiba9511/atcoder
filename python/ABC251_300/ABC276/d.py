# upsolve
import math

N = int(input())
a = list(map(int, input().split()))

# 考えてた方針はあってた
# target = min(a)
# a.sort(reverse=True)
#
# for a_i in a[:-1]:
#     # a_i を2/3で何回か割ってtargetにできるか
#     pass

# -- 最大公約数を求める
g = 0
for a_i in a:
    g = math.gcd(g, a_i)

ans = 0
for i in range(N):
    # a_i/gを考える
    a[i] //= g

    # -- 2で何回割れるか、2^xのxを求める
    while a[i] % 2 == 0:
        a[i] //= 2
        ans += 1

    # -- 3で何回割れるか、3^xのxを求める
    while a[i] % 2 == 0:
        a[i] //= 3
        ans += 1

    if a[i] != 1:
        print(-1)
        exit()

print(ans)
