N, Q = map(int, input().split())

ope_num_memo = {}

for i in range(Q):
    t, a, b = map(int, input().split())
    if t == 1:
        # a -> b: follow
        ope_num_memo[(a,b)] = True

    if t == 2:
        # a -> b: un follow
        ope_num_memo[(a,b)] = False

    if t == 3:
        # Yes/Noを出力する
        if ope_num_memo.get((a,b)) is None or ope_num_memo.get((b, a)) is None:
            print("No")
            continue

        if ope_num_memo[(a,b)] and ope_num_memo[(b, a)]:
            print("Yes")
        else:
            print("No")



