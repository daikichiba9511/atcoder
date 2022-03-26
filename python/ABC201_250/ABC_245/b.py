N = int(input())
A = list(map(int, input().split()))

for a in range(max(A) + 1):
    if a not in A:
        print(a)
        exit()
print(max(A) + 1)
