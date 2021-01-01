# TODO うまく行かないバグを直す

INF = 10 ** 8 # 十分大きな値

# dp テーブルは余裕を持ったサイズにする
dp = [[0]*(1<<20 + 1) for _ in range(21)]

# 入力
N = int(int(input()))
dist = [list(map(int, input().split())) for _ in range(N)]

def rec(bit : int, v : int):
    # すでに探索済みだったらリターン
    if (dp[bit][v] != -1):
        return dp[bit][v]

    # 初期値
    if (bit == (1 << v)):
        dp[bit][v] = 0
        return dp[bit][v]

    # 答えを格納する変数
    res : int = INF

    # bitのvを除いた物
    prev_bit : int = bit & ~(1 << v)

    # v の手間のノードとして　u を全探索
    for u in range(N):
        if not (prev_bit & (1 << u)) : continue # uが　prev_bitになければだめ

        # 再帰的に探索
        if (res > rec(prev_bit, u) + dist[u][v]):
            res = rec(prev_bit, u) + dist[u][v]

    # メモしながらリターン
    dp[bit][v] = res
    return dp[bit][v]

def bit_dp():
    # メモ再帰
    # テーブルを全部−１にしておく。（−１でなかったところは探索済み）
    for bit in range(2**N):
        for v in range(N):
            dp[bit][v] = -1
            

    # 探索
    res = INF
    for v in range(N):
        if (res > rec((1 << N)-1, v)):
            res = rec((1 << N)-1, v)

    print(res)


if __name__ == "__main__":
    # bit_confirm()
    # bit_practice()
    # partial_sum()
    # partial_partial_sum()
    # xor_shift()
    bit_dp()

