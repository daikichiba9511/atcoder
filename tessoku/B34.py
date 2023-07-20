n, x, y = map(int, input().split())
a = list(map(int, input().split()))
grundy_map = {0: 0, 1: 0, 2: 1, 3: 1, 4: 2}
grundies = [grundy_map[a_i % 5] for a_i in a]
xor_sum = 0
for g in grundies:
    xor_sum ^= g
if xor_sum != 0:
    print("First")
else:
    print("Second")
