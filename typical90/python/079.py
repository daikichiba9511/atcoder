H, W = map(int, input().split())

A = [list(map(int, input().split())) for _ in range(H)]
B = [list(map(int, input().split())) for _ in range(H)]

# H,W <= 100
# O(HW)
operations_num = 0
for i in range(H - 1):
    for j in range(W - 1):
        diff = B[i][j] - A[i][j]
        A[i][j] += diff
        A[i][j + 1] += diff
        A[i + 1][j] += diff
        A[i + 1][j + 1] += diff
        operations_num += abs(diff)

if A == B:
    print("Yes")
    print(operations_num)
else:
    print("No")
