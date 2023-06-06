h, w = map(int, input().split())
c = [input() for _ in range(h)]

N = min(h, w)

# # print(c)
# ans = {size: 0 for size in range(1, N + 1)}
# for i in range(h):
#     for j in range(w):
#         if c[i][j] != "#":
#             continue
#         size = 0
#         for d in range(1, N):
#             if i + d >= h or i - d < 0 or j + d >= w or j - d < 0:
#                 continue

#             if c[i + d][j + d] == "#" and c[i + d][j - d] == "#" and c[i - d][j + d] == "#" and c[i - d][j - d] == "#":
#                 # print(i, j, d)
#                 size += 1
#                 # print(i, j, d, size)
#                 if size == 1:
#                     ans[size] += 1
#                 else:
#                     ans[size - 1] -= 1
#                     ans[size] += 1
#                 # print(ans)

#                 # 配列外参照の可能性がある
#                 # i + d + 1 >= h or i + d + 1 >= w => c[i + d + 1][i + d + 1]は配列外参照
#                 # i - d - 1 < 0 or i - d - 1 < 0 => c[i - d - 1][j - d - 1]は配列外参照
#                 # i + d + 1 >= h or i - d - 1 < 0 => c[i + d + 1][i - d - 1]は配列外参照
#                 # i - d - 1 < 0 or i + d + 1 >= w => c[i - d - 1][i + d + 1]は配列外参照
#                 # 逆に考えると
#                 # i + d + 1 < h and i + d + 1 < w => c[i + d + 1][i + d + 1]は配列内参照
#                 # i - d - 1 >= 0 and i - d - 1 >= 0 => c[i - d - 1][j - d - 1]は配列内参照
#                 # i + d + 1 < h and i - d - 1 >= 0 => c[i + d + 1][i - d - 1]は配列内参照
#                 # i - d - 1 >= 0 and i + d + 1 < w => c[i - d - 1][i + d + 1]は配列内参照
#                 if i + d + 1 < h and j + d + 1 < w:
#                     if c[i + d + 1][j + d + 1] == ".":
#                         # print("right_bottom break")
#                         break

#                 if i - d - 1 >= 0 and j - d - 1 >= 0:
#                     if c[i - d - 1][j - d - 1] == ".":
#                         # print("left_top break")
#                         break

#                 if i + d + 1 < h and j - d - 1 >= 0:
#                     if c[i + d + 1][j - d - 1] == ".":
#                         # print("right_top break")
#                         break

#                 if i - d - 1 >= 0 and j + d + 1 < w:
#                     if c[i - d - 1][j + d + 1] == ".":
#                         # print("left_bottom break")
#                         break


# # print(ans)
# print(" ".join(map(str, ans.values())))

from itertools import product


def ok(i, j):
    return 0 <= i < h and 0 <= j < w


def test(i, j, d):
    for x, y in product([-d, d], [-d, d]):
        s, t = i + x, j + y
        # print(i, j, s, t, d, ok(s, t), c[s])
        if not ok(s, t) or c[s][t] != "#":
            return False
    return True


ans = [0] * N
for i, j in product(range(h), range(w)):
    if c[i][j] == ".":
        continue

    # print(i, j)
    if test(i, j, 1):
        # print(i, j)
        d = 1
        while test(i, j, d + 1):
            d += 1
        ans[d - 1] += 1
print(*ans, sep=" ")
