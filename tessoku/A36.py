n, k = map(int, input().split())
if k >= 2 * n - 2 and k % 2 == 0:
    print("Yes")
else:
    print("No")
