"""文字列S,Tの共通部分の最小のもをO(|S||T|)で求める（最長共通部分問題）

dp[i][j] := 文字列Sのi番目の文字と文字列Tのj番目までの文字列のLCS(最長共通部分）

Reference
    * https://atcoder.jp/contests/dp/submissions/14465252

"""
import sys
import numpy as np

read = sys.stdin.buffer.read
readline = sys.stdin.buffer.readline
readlines = sys.stdin.buffer.readlines


def longest_common_subsequence(S: np.ndarray, T: np.ndarray) -> np.ndarray:
    """
    dp[i, j] = LCS(S[:i], T[:j])

    * 左上から： n - 1番目の文字列とTの等しい文字のindexを作って前の行から
    """
    l_s, l_t = len(S), len(T)
    dp = np.zeros((l_s + 1, l_t + 1), np.int32)
    for n in range(1, l_s + 1):
        dp[n, 1:] = dp[n - 1, :-1] + (S[n - 1] == T)  # 左上から同じ文字を数え上げていく
        np.maximum(dp[n], dp[n - 1], out=dp[n])  # 上から行毎に最大値を更新してく
        np.maximum.accumulate(dp[n], out=dp[n])  # 左から列毎に最大値を更新してく
    return dp


def deconstruct_LCS(S: np.ndarray, T: np.ndarray, dp: np.ndarray) -> str:
    """ 右下から戻ってくる
    """
    tmp = []
    i, j = len(S), len(T)
    while i > 0 and j > 0:
        if S[i - 1] == T[j - 1]:
            i, j = i - 1, j - 1
            tmp.append(S[i])

        elif dp[i, j] == dp[i - 1, j]:
            i -= 1

        else:
            j -= 1

    return "".join(reversed(tmp))


def main():
    # decode()で文字列にしてる
    # U1 : unicode文字列で一要素一文字(e.g "U4" => 1.2344 <=> '1.23'
    S = np.array(list(readline().decode()), "U1")
    T = np.array(list(readline().decode()), "U1")

    dp = longest_common_subsequence(S, T)

    print(deconstruct_LCS(S, T, dp))


if __name__ == "__main__":
    main()
