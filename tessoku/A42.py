n, k = map(int, input().split())
ab = [tuple(map(int, input().split())) for _ in range(n)]

ans = 0
for a_min in range(1, 101):
    for b_min in range(1, 101):
        # 下限値が(a_min, b_min)のときに可能な数
        # 範囲を決めて、その中に収まるものを全探索する
        cnt = 0
        for a, b in ab:
            is_a_ok = a_min <= a <= a_min + k
            is_b_ok = b_min <= b <= b_min + k
            if is_a_ok and is_b_ok:
                cnt += 1
        if cnt > ans:
            ans = cnt
print(ans)
