N = int(input())
A = [int(i) for i in input().split()]

# graph = [[] for _ in range(2 * N + 2)]
# for i, a in enumerate(A):
#     graph[a].append(2*i)
#     graph[a].append(2*i + 1)
#
# for k in range(2 * N + 2):
#     todo = [(0, 0)]
#     cnt = 0
#     while todo:
#         d, pos = todo.pop()
#         cnt += 1
#

# 親+1が答え. 分岐されたタイミングで答えを記録しておけばO(N)
ans = [0] * (2 * N + 1)
for i, a in enumerate(A):
    ans[2 * i + 1] = ans[a - 1] + 1
    ans[2 * i + 2] = ans[a - 1] + 1
print(*ans, sep="\n")
