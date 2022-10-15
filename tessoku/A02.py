N, X = map(int, input().split())
A = list(map(int, input().split()))

exists = False
for a in A:
    if a == X:
        exists = True
        break

ans = "Yes" if exists else "No"
print(ans)
