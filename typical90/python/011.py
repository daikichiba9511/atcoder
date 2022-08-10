def main():
    N = int(input())

    table = []
    for _ in range(N):
        # shape: (D, C, S)
        table.append(tuple(map(int, input().split())))

    # Dの昇順でソート
    table.sort(key=lambda x: x[0])
    # j + C[i + 1]でおおきくなりがちなので上限まで容量確保しておくほうが良さそう
    D = [0] * 5009
    C = [0] * 5009
    S = [0] * 5009
    for i in range(N):
        D[i] = table[i][0]
        C[i] = table[i][1]
        S[i] = table[i][2]

    dp = [[0] * 5009 for _ in range(5009)]
    # 動的計画法 O(N^2)
    for i in range(N):
        for j in range(5000):
            # dp[i + 1][j]ははじめ0でinitiallizeされてるのでmaxをとって上書きしてく
            # 仕事iをやらない場合
            dp[i + 1][j] = max(dp[i + 1][j], dp[i][j])
            # 仕事iをやる場合
            # 締切に間に合ってるか
            # j日目+仕事iにかかる日数C_i <= D_i
            if j + C[i] <= D[i]:
                dp[i + 1][j + C[i]] = max(
                    dp[i + 1][j + C[i]], dp[i][j] + S[i]
                )

    ans = 0
    for j in range(5009):
        ans = max(ans, dp[N][j])

    print(ans)


if __name__ == "__main__":
    main()
