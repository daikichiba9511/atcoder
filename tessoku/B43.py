n, m = map(int, input().split())
a = list(map(int, input().split()))

# # O(nm)
# for i in range(1, n + 1):
#     num_not_correct = a.count(i)
#     print(m - num_not_correct)

# i問目を間違えていたら間違えた人に1を足す
# その人が何回間違えたかがわかる
# O(n + m)
ans = [0] * n
for m_i in range(m):
    ans[a[m_i] - 1] += 1

for ans_i in ans:
    print(m - ans_i)

