N = int(input())

st = []
for _ in range(N):
    st.append(input().split())

flag = True
for i in range(N):
    s_i, t_i = st[i]
    flag_s = True
    flag_t = True
    for j in range(N):
        if i == j:
            continue
        s_j = st[j][0]
        t_j = st[j][1]
        if s_i == s_j or s_i == t_j:
            flag_s = False
        if t_i == t_j or t_i == s_j:
            flag_t = False

    if not flag_s and not flag_t:
        flag = False

if flag:
    print("Yes")
else:
    print("No")
