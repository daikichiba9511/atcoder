N = int(input())
P_s = list(map(int, input().split()))

cnt = 1
pp = P_s[N - 2]
if pp == 1:
    print(cnt)
    exit()

while True:
    pp = P_s[pp - 2]
    cnt += 1
    if pp == 1:
        break

print(cnt)
