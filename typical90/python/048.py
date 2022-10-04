# 選択肢を選んだ時の加点の観点で情報の粒度を揃える
N, K = map(int, input().split())
plus_list = []
for _ in range(N):
    a, b = map(int, input().split())
    plus_list.append(b)
    plus_list.append(a - b)

plus_list.sort(reverse=True)
print(sum(plus_list[:K]))
