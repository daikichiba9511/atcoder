BIT_FLAG_0 = (1 << 0) # 0000 0000 0000 0001
BIT_FLAG_1 = (1 << 1) # 0000 0000 0000 0010
BIT_FLAG_2 = (1 << 2) # 0000 0000 0000 0100
BIT_FLAG_3 = (1 << 3) # 0000 0000 0000 1000
BIT_FLAG_4 = (1 << 4) # 0000 0000 0001 0000
BIT_FLAG_5 = (1 << 5) # 0000 0000 0010 0000
BIT_FLAG_6 = (1 << 6) # 0000 0000 0100 0000
BIT_FLAG_7 = (1 << 7) # 0000 0000 1000 0000


def bit_confirm():
    # {1, 3, 5}にフラグの入ったビット
    bit = BIT_FLAG_1 | BIT_FLAG_3 | BIT_FLAG_5
    print("(1,3,5) = {}".format(bin(bit)))

    # bit {1,3, 5}について、３番目のフラグが立っていること
    if (bit & BIT_FLAG_3):
        print("3 is in ", bin(bit))

    #  bit {1,3, 5}について、0番目のフラグが立っていること
    if (bit & BIT_FLAG_0):
        print("3 is in ", bin(bit))

    # 新しいbit {0, 3, 4}
    bit2 = BIT_FLAG_0 | BIT_FLAG_3 | BIT_FLAG_4
    print(bin(bit2))
    print(bin(bit & bit2))
    print(bin(bit | bit2))

    # bitに6番目のフラグを立てる
    print("before:",bin(bit))
    bit |= BIT_FLAG_6
    print("before:",bin(bit), "(6 inclueded)")

    # bit2から3番目のフラグを消す
    print("before:",bin(bit2))
    bit2 &= ~BIT_FLAG_3
    print("after:",bin(bit2), "(3 exclueded)")

from typing import List, Union

Num = Union[int, float]
Vector = List[Num]

def bit_practice():
    # 部分集合族
    n : int = 5

    # {0, 1, ... , n-1}の部分集合の全探索
    for s in range(2**n):
        # bit の表す集合を求める。
        S : Vector = []
        for i in range(n):
            if (s & (1<<i)):
                S.append(i)

        # bitの表す集合の出力
        print(s, ": {", end="")
        for i in range(len(S)):
            print(S[i], end=" ")
        print("}")

def partial_sum():
    n = 3
    a = (7, 2, 9)
    K = 11

    exist : bool = False
    for bit in range(2*n):
        # bitの表す集合を求める
        s : int = 0
        for i in range(n):
            if (bit & (1<<i)):
                s += a[i]
        
        # sum が　K　に一致するか
        if s == K:
            exist = True
        
    if exist:print("Yes")
    else:print("No")

def partial_partial_sum():
    n : int = 10
    A = (1<<2) | (1<<3) | (1<<5) | (1<<7)
    bit = A
    while True:
        S : Vector = []
        for i in range(n):
            if (bit & (1<<i)):
                S.append(i)

        # bit の表す集合の出力
        print(bit, ": {", end="")
        for i in range(len(S)):
            print(S[i], end=" ")
        print("}")

        # 最後の０でbreak
        if bit == 0:
            break

        bit = (bit - 1) & A

def xor_shift():
    # 全部５にしかならない。。
    def randInt():
        tx : int = 123456789; ty : int = 362436069; tz : int = 521288629;  tw : int = 88675123
        tt : int = tx^(tx<<11)
        tx = ty; ty = tz; tz = tw
        return (tw^(tw>>19))^(tt^(tt>>8))
    for i in range(100):
        print( (randInt() % 6 + 1 ), ", ", end=" ")
        if (i % 10 == 0):
            print()
    return 0

# TODO うまく行かないバグを直す
INF = 10 ** 8 # 十分大きな値
# dp テーブルは余裕を持ったサイズにする
dp = [[0]*(1<<20 + 1) for _ in range(21)]
def rec(bit : int, v : int):
    # すでに探索済みだったらリターン
    if (dp[bit][v] != -1):
        return dp[bit][v]

    # 初期値
    if (bit == (1 << v)):
        dp[bit][v] = 0

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
    return res

def bit_dp():
    # メモ再帰
    # 入力
    N = int(int(input()))
    dist = [list(map(int, input().split())) for _ in range(N)]

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


