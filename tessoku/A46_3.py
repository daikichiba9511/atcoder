import math
import random

# import numpy as np

# np.random.seed(0)


def dist(x, y, p: int, q: int) -> float:
    return ((x[p] - x[q]) ** 2 + (y[p] - y[q]) ** 2) ** 0.5


def score_fn(x, y, path, n):
    score = sum(dist(x, y, path[i] - 1, path[i + 1] - 1) for i in range(n))
    return score


def main():
    n = int(input())
    x, y = [], []
    for _ in range(n):
        x_i, y_i = map(int, input().split())
        x.append(x_i)
        y.append(y_i)
    path = list(range(1, n + 1)) + [1]
    # path = np.arange(1, n + 2)
    # path[-1] = 1
    # print(path)
    score = score_fn(x, y, path, n)
    init_score = score

    # 焼きなまし法, minimize
    t_max = 100_000
    for t in range(t_max):
        # l = np.random.randint(2, n - 1)
        # r = np.random.randint(l + 1, n)

        l = random.randint(2, n - 1)
        r = random.randint(l + 1, n)

        # swap path[l:r] more faster...
        new_path = path[:l] + path[l:r][::-1] + path[r:]
        # new_path = np.concatenate([path[:l], path[l:r][::-1], path[r:]])
        new_score = score_fn(x, y, new_path, n)

        T = 30.0 - 28.0 * t / float(t_max)
        delta = score - new_score
        if delta > 0:
            score = new_score
            path = new_path
            continue

        # print(prob, score, new_score)
        # if np.random.rand() * np.log(T) < delta:
        if random.random() * math.log(T) < delta:
            score = new_score
            path = new_path

    for p_i in path:
        print(p_i)
    # print(f"init score: {init_score}, final score: {score}")


if __name__ == "__main__":
    main()
