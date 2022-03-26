a, b, c, d = tuple(map(int, input().split()))

if a < c:
    print("Takahashi")
else:
    if a == c and b <= d:
        print("Takahashi")
    else:
        print("Aoki")
