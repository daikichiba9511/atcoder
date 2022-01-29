
N = int(input())

A = list(map(int, input().split()))

A.sort()
for i in range(1, N+1):
    cnt = A.count(i)
    if cnt != 4:
        print(i)
        break
