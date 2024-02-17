import heapq

n, m = map(int, input().split())
INF = 10 ** 18
g = [[] for _ in range(n)]
for _ in range(m):
    a,b,c=map(int,input().split())
    a-=1
    b-=1
    g[a].append((b,c))
    g[b].append((a,c))

que=[]
kakutei=[False]*n
cur=[INF]*n
cur[0]=0
heapq.heappush(que,(cur[0],0))
prev=[-1]*n

# dijkstra, O(MlogM)
while que:
    pos = heapq.heappop(que)[1]
    if kakutei[pos]:
        continue
    kakutei[pos] = True
    for nex, cost in g[pos]:
        if cur[nex] > cur[pos] + cost:
            cur[nex] = cur[pos] + cost
            heapq.heappush(que, (cur[nex], nex))
            prev[nex] = pos

# 経路復元
ans = []
pos = n - 1
while True:
    v = prev[pos]
    ans.append(pos + 1)
    if v == -1:
        break
    pos = v
print(*ans[::-1])
