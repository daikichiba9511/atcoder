import math

a, b = map(int, input().split())

r = a * b // math.gcd(a, b)

if r <= pow(10, 18):
    print(r)
else:
    print("Large")
