N, L = map(int, input().split())

dp_table = [0] * (N + 1)
dp_table[0] = 1
for i in range(1, N + 1):
    if i < L:
        dp_table[i] = dp_table[i - 1]
    else:
        dp_table[i] = (dp_table[i - 1] + dp_table[i - L]) % 1_000_000_007

print(dp_table[N])
