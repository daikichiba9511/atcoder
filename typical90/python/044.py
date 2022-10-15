n, q = map(int, input().split())

a = list(map(int, input().split()))


t2_memo = 0
for _ in range(q):
    t, x, y = map(int, input().split())
    x -= 1
    y -= 1
    if t == 1:
        # nを越えないように余りでindexを指定
        # これで順繰りにアクセスできる
        a[(x + t2_memo) % n] = a[(y + t2_memo) % n]
        a[(y + t2_memo) % n] = a[(x + t2_memo) % n]
        continue

    if t == 2:
        t2_memo = (t2_memo + n - 1) % n
        continue

    print(a[(x + t2_memo) % n])
