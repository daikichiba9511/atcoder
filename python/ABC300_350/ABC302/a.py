a, b = map(int, input().split())

r = a % b
if r == 0:
    print(a // b)
else:
    print(a // b + 1)
