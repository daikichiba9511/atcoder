from heapq import heapify, heappop, heappush
# 1<=n<=2*10**5
# 1<=t_i,d_i<=10**18
n = int(input())
lr = []
for _ in range(n):
    ti, di = map(int, input().split())
    lr.append((ti, di + ti))
lr.sort(key=lambda x: x[0])
# print(lr)

ans = 0
it = 0
pq = []  # rを管理する
heapify(pq)
curr = 1
# selected = []
while True:
    # print(f"############### {curr = } ####################")
    if len(pq) == 0:
        if it == n:
            break
        curr = lr[it][0]

    # ノードnまで探索, 現段階で選べるものをpqに入れる
    while it < n and lr[it][0] == curr:
        heappush(pq, lr[it][1])
        it += 1

    # print("it: ", it)
    # print("Current: ", curr, "pq: ", pq, "lr", lr)

    # pqの中で最小のものを選ぶ
    if len(pq) > 0:
        p_ = heappop(pq)
        # selected.append(p_)
        ans += 1

    curr += 1

    # 区間を抜けてるものはスキップ
    while len(pq) > 0 and pq[0] < curr:
        # print("Discard: ", pq[0])
        heappop(pq)
    # print(f"{curr = } {pq = }")



# print(selected)
print(ans)
