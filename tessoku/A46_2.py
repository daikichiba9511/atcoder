import numpy as np

np.random.seed(0)

n = int(input())
x, y = [], []
for _ in range(n):
    x_i, y_i = map(int, input().split())
    x.append(x_i)
    y.append(y_i)


def dist(x: list[int], y: list[int], p: int, q: int) -> float:
    return ((x[p] - x[q]) ** 2 + (y[p] - y[q]) ** 2) ** 0.5


def score_fn(x, y, path):
    score = 0
    for i in range(n - 1):
        score += dist(x, y, path[i] - 1, path[i + 1] - 1)
    return score


path = list(range(1, n + 1))
score = score_fn(x, y, path)
init_score = score
# 山登り法

for t in range(20_000):
    l = np.random.randint(2, n)
    r = np.random.randint(2, n)
    if l > r:
        l, r = r, l
    new_path = path[:l] + path[l:r][::-1] + path[r:]
    new_score = score_fn(x, y, new_path)
    if new_score < score:
        path = new_path
        score = new_score

for p_i in path:
    print(p_i)
print(1)

# print(f"init score: {init_score}")
# print(f"final score: {score}")
