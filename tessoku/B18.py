N, S = map(int, input().split())
A = list(map(int, input().split()))

dp = [[False] * (S + 9) for _ in range(N + 1)]

# dpで達成できる部分和を列挙する
dp[0][0] = True
for i in range(1, N + 1):
    for s in range(S + 1):
        if s >= A[i - 1]:
            if dp[i - 1][s] or dp[i - 1][s - A[i - 1]]:
                dp[i][s] = True
            else:
                dp[i][s] = False

        else:
            if dp[i - 1][s]:
                dp[i][s] = True
            else:
                dp[i][s] = False

if not dp[N][S]:
    print(-1)
    exit()

# 復元
# 後ろからカードiを選ぶかどうか
pos = S
ans = []
for i in range(N, 0, -1):
    # カードiを選ばない時(このi=k~k+lのTrueは選ばないことで達成されてるTrue)
    # カードiを選ばないことで部分和posが達成できないときが来る
    # この時はカードiを選んでs-A[i]からsに遷移してきたってこと
    if dp[i - 1][pos]:
        # 部分和は変化しない
        pos = pos
    else:
        pos = pos - A[i - 1]
        ans.append(i)

print(len(ans))
print(" ".join(map(str, ans[::-1])))
