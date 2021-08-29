N = int(input())

ST = []
for _ in range(N):
    s_t, t_t = input().split()
    ST.append((s_t, t_t))

# O(N^2)
flag = False
for s_i, t_i in ST:
    same_s = [(i, j) for i, j in ST if i == s_i]
    same_t = [(i, j) for i, j in same_s if j == t_i]
    if len(same_t) - 1 > 0:  # -1: s_i double count
        flag = True
        break

if flag:
    print("Yes")
else:
    print("No")




