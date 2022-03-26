a, b, c, x = tuple(map(int, input().split()))

if x <= a:
    print(1.0)

elif a < x <= b:
    print(c / (b - a))

else:
    print(0.0)
