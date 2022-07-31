N = map(int, input())
A = list(map(int, input().split(" ")))
B = list(map(int, input().split(" ")))


# 昇順にソート
A.sort()
B.sort()

s = 0
for a, b in zip(A, B):
    diff = abs(a - b)
    s += diff

print(s)
