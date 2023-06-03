# n, m = map(int, input().split())
# s = [input() for _ in range(n)]
# if m == 1:
#     print("Yes")
# else:
#     s.sort()
#     for i in range(len(s) - 1):
#         for j in range(len(s[i])):
#             t = s[i][:j] + s[i + 1][j] + s[i][j + 1 :]
#             if t == s[i + 1]:
#                 print("Yes")
#                 exit()
#     print("No")

import itertools


def count_diff(a, b):
    cnt = 0
    for a_i, b_i in zip(a, b):
        if a_i != b_i:
            cnt += 1
    return cnt


n, m = map(int, input().split())
s = [input() for _ in range(n)]
s.sort()

for t in itertools.permutations(s):
    ok = True
    for i in range(n - 1):
        if count_diff(t[i], t[i + 1]) != 1:
            ok = False
    if ok:
        print("Yes")
        exit()
print("No")
