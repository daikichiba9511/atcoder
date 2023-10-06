n = int(input())
x, y = [], []
for _ in range(n):
    x_i, y_i = map(int, input().split())
    x.append(x_i)
    y.append(y_i)


def dist(x: list[int], y: list[int], p: int, q: int) -> float:
    return ((x[p] - x[q]) ** 2 + (y[p] - y[q]) ** 2) ** 0.5


p = [i for i in range(n)]
current_place = 1
visited = [False] * n
visited[0] = True
p[0] = 1

for i in range(2, n + 1):
    # 一番近い点を探す
    min_dist, min_point = float("inf"), -1

    # 距離の探索
    for j in range(1, n + 1):
        if visited[j - 1]:
            continue

        # 今いる点からP_jまでの距離を求める
        seeking_dist = dist(x, y, current_place - 1, j - 1)
        if seeking_dist < min_dist:
            min_dist = seeking_dist
            min_point = j

    # 次の探索点の決定＆更新
    visited[min_point - 1] = True
    p[i - 1] = min_point
    current_place = min_point

for p_i in p:
    print(p_i)
print(1)
# print(sum(dist(x, y, p[i - 1] - 1, p[i] - 1) for i in range(n)))
