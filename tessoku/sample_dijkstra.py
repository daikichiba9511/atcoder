INF = 10 ** 18
n = 5
G = [(1, 1), (2, 4)]

kakutei = [False] * n
cur = [INF] * n

# 最短距離を更新していく
while True:
    # [ 操作 A ]: 次に確定する頂点posを決める
    pos = -1
    min_dist = INF
    for i in range(n):
        if kakutei[i] or min_dist <= cur[i]:
            continue
        pos = i
        min_dist = cur[i]

    # 次に確定する頂点がない場合は終了
    if pos == -1:
        break

    # [ 操作 B ]: posと隣接する頂点のcurの値を更新する
    kakutei[pos] = True
    for i in range(len(G[pos])):
        nex = G[pos][i][0]
        cost = G[pos][i][1]
        cur[nex] = min(cur[nex], cur[pos] + cost)
