"""
桁DP?

dp[i][j] := 上からi桁目の時点でmodで割った余りjの場合の数

"""
MOD = 998244353
N = int(input())

dp = [[0] * MOD for _ in range(10)]

dp[0][0] = 0

    

