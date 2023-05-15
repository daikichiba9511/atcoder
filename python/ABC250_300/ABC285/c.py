S = input().lower()
l = len(S)

# 26進数として数える
# 1 ~ l-1までの場合の数の総数 = 26^1 + 26^2 + ... + 26^{l-1}
res, add = 0, 26
for i in range(1, l):
    res += add
    add *= 26

# 長さlの中で何番目かを求める
num = 0
for s in S:
    num *= 26
    num += ord(s) - ord("a")
print(res + num + 1)
