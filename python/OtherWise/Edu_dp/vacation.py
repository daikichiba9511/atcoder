
def main():
    N = int(input())
    p_list = []
    for _ in range(N):
        p_list.append(list(map(int, input().split())))

    # initialize dp table
    dp = [[0]*3 for _ in range(N+2)]

    for i in range(N):
        for j in range(3):
            for k in range(3):
                if j == k: continue # can't seclect same choice
                tmp_cost = dp[i][j] + p_list[i][k]
                if dp[i + 1][k] < tmp_cost:
                    dp[i + 1][k] = tmp_cost

    # every chain has maximize sum
    res = 0
    for j in range(3):
        if res < dp[N][j]:
            res = dp[N][j]
    print(res)

if __name__ == "__main__":
    main()