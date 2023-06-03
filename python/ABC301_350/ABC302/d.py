n, m, d = map(int, input().split())
a = list(map(int, input().split()))
b = list(map(int, input().split()))
if len(a) == 0 or len(b) == 0:
    print(-1)

# O(NlogN), O(MlogM)
a.sort()
b.sort()

# choise the maximum element
while True:
    if len(a) == 0 or len(b) == 0:
        print(-1)
        break

    a0 = a[-1]
    b0 = b[-1]

    if abs(a0 - b0) <= d:
        print(a0 + b0)
        break
    else:
        if a0 < b0:
            b.pop()
        else:
            a.pop()
