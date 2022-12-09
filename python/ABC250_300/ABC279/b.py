N = int(input())
S = list(map(int, input().split()))

ans = []
for i in range(len(S)):
    if i == 0:
        ans.append(S[0])
    else:
        ans.append(S[i] - S[i - 1])
print(*ans)
