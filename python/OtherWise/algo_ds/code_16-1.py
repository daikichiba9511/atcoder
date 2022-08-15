from typing import Final, List


class Edge:
    """辺を表すクラス

    Args:
        r: 逆辺(to, from)がG[to]の何番目の要素か
        c: 辺(from, to) の容量

    """

    def __init__(self, r: int, f: int, t: int, c: int) -> None:
        self.rev = r
        self.frm = f
        self.to = t
        self.cap = c


class Graph:
    """Graphを表すクラス

    Args:
        n: 頂点数
    """

    # 隣接リスト
    _list: List[List[Edge]]

    def __init__(self, n: int):
        self._list = [[] for _ in range(n)]

    def size(self) -> int:
        return len(self._list)

    def __len__(self) -> int:
        return len(self._list)

    def __getitem__(self, v) -> List[Edge]:
        """GraphインスタンスをGとして、G._list[v]をG[v]でかけるようにする"""
        return self._list[v]

    def redge(self, e: Edge):
        """辺e=(u,v)の逆辺(v,u)を取得する"""
        return self._list[e.to][e.rev]

    def run_flow(self, e: Edge, f: int) -> None:
        """辺e=(u,v)に流量fのフローを流す
        e=(u,v)の流量がfだけ減少する、この時逆辺(v,u)の流量を増やす
        """
        e.cap -= f
        self.redge(e).cap += f

    def addedge(self, frm: int, to: int, cap: int) -> None:
        """頂点fromから頂点toへ容量capの辺を張る
        この時toからfromへも容量0の辺を張る

        """
        fromrev = len(self._list[frm])
        torev = len(self._list[to])
        self._list[frm].append(Edge(r=torev, f=frm, t=to, c=cap))
        self._list[to].append(Edge(r=fromrev, f=frm, t=to, c=cap))


class FordFulkerson:
    INF: Final[int] = 1 << 30

    def __init__(self) -> None:
        self._seen: List[bool] = []

    def fodfs(self, g: Graph, v: int, t: int, f: int) -> int:
        """残余グラフ上でs-tパスを見つける（深さ優先探索）
        返り値はs-tパス上の容量の最小値（見つからなかったら0）
        f: sからvへ到達した各辺の容量の最小値

        """

        # 終端tに到達したらリターン
        if v == t:
            return f

        self._seen[v] = True
        for e in g[v]:
            if self._seen[e.to]:
                continue

            # 容量0の辺は実際に存在しない
            if e.cap == 0:
                continue

            # s-tパスを探す
            # 見つからなかったらflowはパス上の容量
            # 見つからなかったら0
            flow = self.fodfs(g, e.to, t, min(f, e.cap))

            # 見つからなかったら次辺を探す
            if not flow:
                continue

            # 辺eに容量flowのフローを流す
            g.run_flow(e, flow)

            # s-tパスを見つけたらパス上最小容量を返す
            return flow

        # s-tパスが見つからなかったことを示す
        return 0

    def solve(self, g: Graph, s: int, t: int) -> int:
        """グラフg上のs-t間の最大流量を求める
        ただしリターン時にgは残余グラフになる

        """
        res = 0

        # 残余グラフにs-tパスがなくなるまで反復
        while True:
            self._seen = [False] * len(g)

            flow = self.fodfs(g, s, t, self.INF)

            # 見つからなかったら終了
            if not flow:
                return res

            # 答えを加算
            res += flow


def main():
    n, m = map(int, input().split())

    g = Graph(n)
    for _ in range(m):
        u, v, c = map(int, input().split())
        # 容量cの辺(u, v)を張る
        g.addedge(frm=u, to=v, cap=c)

    ff = FordFulkerson()
    print(ff.solve(g, s=0, t=n - 1))
