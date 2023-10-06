n = int(input())
# O(n^2)
a = [list(map(int, input().split())) for _ in range(n)]
q = int(input())

state = list(range(n))
# O(q)
for _ in range(q):
    t, x, y = map(int, input().split())
    if t == 1:  # 交換操作
        state[x - 1], state[y - 1] = state[y - 1], state[x - 1]
    else:  # 取得操作
        print(a[state[x - 1]][y - 1])
