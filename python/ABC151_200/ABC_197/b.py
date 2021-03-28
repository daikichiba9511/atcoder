""" https://atcoder.jp/contests/abc197/tasks/abc197_b

* 計算量O(HW) 与えられた始点に対して行Wと列Hの探索
"""
import sys


def main():
    def input():
        return sys.stdin.readline()[:-1]

    H, W, Y, X = tuple(map(int, input().split()))
    graph = [list(input()) for _ in range(H)]
    H -= 1
    W -= 1
    X -= 1
    Y -= 1
    # 同じ行、または列を始点(x, y)から終点(w, v)を選んでその間に'#'がなければ選んだ点(w, v)は見えるます
    res = 1
    dx = [0, 1, 0, -1]
    dy = [-1, 0, 1, 0]

    for d in range(4):
        x = X
        y = Y
        while True:
            x += dx[d]
            y += dy[d]

            # 外にでたら終了
            if x < 0 or W <= x or y < 0 or H <= y:
                break

            # 行き止まりなら終了
            if graph[y][x] == "#":
                break
            res += 1

    print(res)


if __name__ == "__main__":
    main()
