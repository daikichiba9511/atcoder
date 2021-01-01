from typing import List, Union

Graph = List[List[int]]

def base_dfs(G : Graph, v : int, seen : List[bool]):
    # v を訪問済みにする
    seen[v] = True

    # vから行ける各頂点 next_v について
    for next_v in G[v]:
        # 探索済みだったらスルー
        if (seen[next_v]) : continue
        # 再帰的に探索
        base_dfs(G, next_v, seen)


def base():
    n, m, s , t = map(int, input().split())

    # graph 入力受取
    G : Graph = [[0]*n for _ in range(n)]
    for _ in range(m):
        a, b = map(int, input().split())
        G[a].append(b)

    # 頂点をsをスタートとした探索
    seen : List[bool] = [False] * n
    base_dfs(G, s, seen)

    # tにたどり着けるかどうか
    if (seen[t]) : print("Yes")
    else : print("No")

def atc_dfs(
    h : int, w : int,
    dx : List[int], dy : List[int] ,
    seen : List[List[bool]], field : List[str]
):
    seen[h][w] = True

    # 四方向を探索
    for dir in range(4):
        nh : int = h + dx[dir]
        nw : int = w + dy[dir]

        # 場外にアウトしたり、移動先が壁の場合はスルー
        if nh < 0 or nh >= h or nw < 0 or nw >= w : continue
        if field[nh][nw] == "#" : continue

        # 移動先が探索済みの場合
        if seen[nh][nw] : continue

        # 移動先が探索済みの場合
        if seen[nh][nw] : continue

        # 再帰的に探索
        atc_dfs(nh, nw, dx, dy, seen, field)


def atc():
    dx = [1, 0, -1, 0]
    dy = [0, 1, 0, -1]
    h, w = map(int, input().split())
    field : List[str] = [input() for _ in range(h)]

    # sとgのマスを特定する
    sh : int = 0 ; sw : int = 0 ; gh : int = 0 ; gw : int = 0
    for i in range(h):
        for j in range(w):
            if field[i][j] == "s" :
                sh = i
                sw = j
            if field[i][j] == "g" :
                gh = i
                gw = j

    # 探索開始
    seen : List[List[bool]] = [[False] * 510 for _ in range(510)]
    atc_dfs(sh, sw, dx, dy, seen, field)

    # 結果
    if seen[gh][gw] : print("Yes")
    else : print("No")

# 二部グラフ判定
# color[v] = 1(黒確定), 0(白確定), -1(未訪問)
def binary_bfs(G : Graph, v : int, color : List[int] , cur : int = 0):
    color[v] = cur
    for next_v in G[v]:
        # 隣接頂点がすでに色確定していた時
        if color[next_v] != -1 :
            # 同じ色が隣接していたらだめ
            if color[next_v] == cur :
                return False
            continue

        # 隣接頂点の色を変えて、再帰的に探索(一回でも　False　が帰ってきら　False)
        if not binray_dfs(G, next_v, color, 1 - cur):
            return False

    return True

def binary():
    # 各頂点と辺数
    n, m = map(int, input().split())

    color = [-1] * n

    # グラフ入力数
    G : Graph = [[0] * n for _ in range(n)]
    for _ in range(m):
        a, b = map(int, input().split())
        G[a].append(b)
        G[b].append(a)

    is_bipartite : bool = True
    for v in range(n):
        if color[v] != -1 : continue # 探索済みならスルー
        if not binary_bfs(G, color, v) :
            is_bipartite = False
    if is_bipartite : print("Yes")
    else : print("No")

from typing import List, Union
Graph = List[List[int]]

# 木上のDFSのテンプレ
def dfs_on_tree(G : Graph, v : int, p : int) :
    for nv in G[v]:
        if nv == p : continue # nv が親　pだったらスルー
        dfs_on_tree(G, nv, p) # v は新たにnvの親になる

def dfs_tree_main():
    n : int = int(input())

    # グラフ入力
    G : Graph = [[] * n for _ in range(n)]
    for _ in range(n-1):
        a, b = map(int, input().split())
        G[a].append(b)
        G[b].append(a)

    # 探索
    root : int = 0 # 仮に頂点０を根とする
    dfs_on_tree(G, root, -1)

def partial_tree_dfs(G : Graph, v : int, p : int, d : int, depth : List[int]):
    depth[v] = d
    for nv in G[v]:
        if nv == p : continue # nv が　親pだったらスルー
        partial_tree_dfs(G, nv, v, d+1, depth) # d を　１増やして子ノードへ


# 根つき木の深さと部分木サイズ
from typing import List, Union
Graph = List[List[int]]

def subtree_dfs(
    G : Graph, v : int, p : int, d : int, depth : List[int], subtree_size : List[int]
):
    depth[v] = d
    for nv in G[v]:
        if nv == p : continue # nv が　親　pだったらスルー
        subtree_dfs(G, nv, v, d + 1, depth, subtree_size)
    
    # 帰りがけ時に部分木サイズを求める
    subtree_size[v] = 1 # 自分自身
    for c in G[v] :
        if c == p : continue
        subtree_size[v] += subtree_size[c] # このサイズを加える
    
def subtree_main():
    # 頂点数　（木なので辺数はNー1で確定
    n = int(input())

    # グラフ
    G : Graph = [[] * n for _ in range(n)]
    for _ in range(n-1):
        a, b = map(int, input().split())
        G[a].append(b)
        G[b].append(a)

    # 探索
    root : int = 0 # 仮に頂点０を根とする
    depth = [0] * n
    subtree_size = [0] * n
    subtree_dfs(G, root, -1, 0, depth, subtree_size)

    # 結果
    for v in range(n):
        print(v, ": depth = ", depth[v], ", subtree_size = ", subtree_size[v])

if __name__ == "__main__":
    binary()