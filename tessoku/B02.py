A, B = map(int, input().split())
exists = False
for i in range(A, B + 1):
    if 100 % i == 0:
        exists = True

print("Yes" if exists else "No")
