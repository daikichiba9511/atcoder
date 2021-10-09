def rot(S):
    """回転"""
    return list(zip(*S[::-1]))


def find_left_top(S):
    """左上が#の座標"""
    for i in range(N):
        for j in range(N):
            if S[i][j] == "#":
                return i, j


def is_same(S, T, N):
    """平行移動して同じか"""
    Si, Sj = find_left_top(S)
    Ti, Tj = find_left_top(T)
    offset_i = Ti - Si
    offset_j = Tj - Sj
    # 差分を固定して始点を移動
    for i in range(N):
        for j in range(N):
            ii = i + offset_i
            jj = j + offset_j
            # Tの座標が範囲内に収まってる時
            if 0 <= ii < N and 0 <= jj < N:
                # 並行移動させながら同じであるべきところが違ったら一致しない
                if S[i][j] != T[ii][jj]:
                    return False
            # N <= ii or N <= jj
            else:
                # 始点が左上の'#'でN <= ii or N <= jjの時は一致しない
                if S[i][j] == "#":
                    return False
    return True


N = int(input())

S = [input() for _ in range(N)]
T = [input() for _ in range(N)]

cntS = sum(1 for i in range(N) for j in range(N) if S[i][j] == "#")
cntT = sum(1 for i in range(N) for j in range(N) if T[i][j] == "#")

if cntS != cntT:
    print("No")
    exit()

# 90度回転を４回行うから
for _ in range(4):
    if is_same(S, T, N):
        print("Yes")
        exit()
    S = rot(S)
print("No")
