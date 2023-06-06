N = int(input())

S = [input() for _ in range(N)]

flag = True
# -- １つ目の条件
for s in S:
    if s[0] not in {"H", "D", "C", "S"}:
        print("No")
        exit()

# -- 2つ目の条件
for s in S:
    if s[1] not in {"A", "2", "3", "4", "5", "6", "7", "8", "9", "T", "J", "Q", "K"}:
        print("No")
        exit()

# -- 3つ目の条件
if len(set(S)) != len(S):
    print("No")
    exit()

print("Yes")
