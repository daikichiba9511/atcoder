from typing import List


def mysolution():
    """ 間違えてる
    """
    H, W = list(map(int, input().split()))
    Q = int(input())

    # 白=>0, 赤=>1
    table = [[0] * W for _ in range(H)]
    for _ in range(Q):
        query = list(map(int, input().split()))
        # t_i = 1: 赤マスを増やす
        if query[0] == 1:
            r_i, c_i = query[1:]
            table[r_i - 1][c_i - 1] = 1
        # t_i = 2: 条件判定
        else:
            ra_i, ca_i, rb_i, cb_i = query[1:]
            print("table: \n", table)
            if table[ra_i - 1][ca_i - 1] and table[rb_i - 1][cb_i - 1]:
                # 到達可能判定
                # [上、右、下、左]
                dydx = [(-1, 0), (0, 1), (1, 0), (0, -1)]

                # 何手でいけるかの手数を記録する
                dp = [[-1] * W for _ in range(H)]
                dp[ra_i - 1][ca_i - 1] = 0
                for i in range(H):
                    for j in range(W):
                        if table[i][j]:
                            for dy, dx in dydx:
                                if i + dy >= H or j + dx >= W:
                                    continue
                                if table[i + dy][j + dx]:
                                    # chmin
                                    dp[i + dy][j + dx] = min(dp[i + dy][j + dx], dp[i][j] + 1)
                # 目標地点が到達可能であれば初期値以外のはず
                print("dp table:\n", dp)
                print()

                if dp[rb_i - 1][cb_i - 1] != -1:
                    print("Yes")
                else:
                    print("No")
                print(" \n ############### \n ")
            else:
                print("No")
                print(" \n ############### \n ")


class UnionFind:
    """ Union Find Tree
    Ref:
        * https://at274.hatenablog.com/entry/2018/02/02/173000
    """
    def __init__(self, n: int) -> None:
        self.parents = [i for i in range(n + 1)]
        self.rank = [0] * (n + 1)

    def find(self, x: int) -> int:
        """ 検索

        親をたどって根を探す

        """
        if self.parents[x] == x:
            return x

        else:
            # 一致したら上書きして返す
            self.parents[x] = self.find(self.parents[x])
            return self.parents[x]

    def unite(self, x: int, y: int) -> None:
        """ 併合
        """
        x = self.find(x)
        y = self.find(y)
        if self.rank[x] < self.rank[y]:
            self.parents[x] = y
        else:
            self.parents[y] = x
            if self.rank[x] == self.rank[y]:
                self.rank[x] += 1

    def are_same(self, x: int, y: int) -> bool:
        """ 同じ集合に属するか判定
        """
        return self.find(x) == self.find(y)


def query1(uf: UnionFind, table: List[List[bool]], px: int, py: int, W: int) -> None:
    # [上、右、下、左]
    dydx = [(-1, 0), (0, 1), (1, 0), (0, -1)]
    for dy, dx in dydx:
        if not table[py + dy][px + dx]:
            continue

        # point
        # hashでどの座標であるか識別できる
        hash1 = (px - 1) * W + (py - 1)
        hash2 = (px + dx - 1) * W + (py + dy - 1)
        # 隣接してる点をuniteしておく
        uf.unite(hash1, hash2)
    # (px, py)は赤
    table[py][px] = True


def query2(uf: UnionFind, table: List[List[bool]], px: int, py: int, qx: int, qy: int, W: int) -> bool:
    if not table[py][px] or not table[qy][qx]:
        return False

    hash1 = (px - 1) * W + (py - 1)
    hash2 = (qx - 1) * W + (qy - 1)
    # (px, py)と(qx, qy)同じグループかを判定、同じグループならつながってるので到達可能
    # if (px, py) and (qx, qy) are same group, enable to go to (qx, qy) from (px, py)
    if uf.are_same(hash1, hash2):
        return True
    return False


def solve():
    """
    連結成分はUnionFind

    Ref:
        * https://twitter.com/e869120/status/1381739128291614720/photo/1
    """
    H, W = list(map(int, input().split()))
    Q = int(input())

    uf = UnionFind(H * W)
    table = [[False] * (2009) for _ in range(2009)]
    for _ in range(Q):
        query = list(map(int, input().split()))
        if query[0] == 1:
            px, py = query[1:]
            query1(uf, table, px, py, W)
        else:
            px, py, qx, qy = query[1:]
            is_able = query2(uf, table, px, py, qx, qy, W)
            if is_able:
                print("Yes")
            else:
                print("No")


def main():
    # mysolution()
    solve()


if __name__ == "__main__":
    main()
