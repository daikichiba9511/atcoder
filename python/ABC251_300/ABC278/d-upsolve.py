# 最後に代入があったところからの差分を考える

N = int(input())
A = list(map(int, input().split()))
Q = int(input())

# Aで数列への代入の差分を管理する
# はじめは全要素が代入から差分がないと考える
non_zero_indices = list(range(N))

# 代入があった時の情報を管理する
base = 0

for _ in range(Q):
    q = input()
    t = int(q[0])
    if t == 1:
        # 差分が0ではない部分を削除
        for i in range(len(non_zero_indices)):
            A[non_zero_indices.pop()] = 0

        # 全要素にx_qを代入するのでbaseを更新する
        base = int(q[2])

    elif t ==2:
        # i_q番目の差分にx_qを加える
        # 最後に代入があったところからどの程度差分があるかをAで管理
        # どの部分に差分があるかをnon_zero_indicesで管理する
        # これによって出力する時にどの部分にどの程度最後に代入があったところからの差分があるかを求められる
        i_q, x_q = int(q[2]), int(q[4])
        A[i_q - 1] += x_q
        non_zero_indices.append(i_q - 1)

    else:
        # baseにindex番目の差分を加える
        _, i_q = map(int, q.split())
        print(base + A[i_q])
