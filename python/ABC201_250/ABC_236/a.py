s = input()
s = list(s)
a, b = tuple(map(int, input().split()))
tmp_a = s[a - 1]
s[a - 1] = s[b - 1]
s[b - 1] = tmp_a
print("".join(s))
