from collections import deque, defaultdict
N = int(input())

graph = defaultdict(list)
for _ in range(N):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)


que = deque()
que.append(1)
S = {1}

# -- DFSで全頂点回って最大値を決める O(|V|)
while que:
    pos = que.popleft()
    for i in graph[pos]:
        if i not in S:
            que.append(i)
            S.add(i)

print(max(S))
