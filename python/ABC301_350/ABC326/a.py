x, y = map(int, input().split())

res = y - x
if -3 <= res <= 2:
    print("Yes")
else:
    print("No")
