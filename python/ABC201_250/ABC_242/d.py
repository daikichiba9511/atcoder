S = input()
Q = int(input())

def change_state(s):
    res = ""
    for i in s:
        if i == "A":
            res += "BC"
        elif i == "B":
            res += "CA"
        else:  # i == "C"
            res += "AB"
    return res


s_states = []
for i in range(Q):
    if i == 0:
        s_states.append(S)
    s_states.append(change_state(s_states[i - 1]))


for i in range(Q):
    t, k = tuple(map(int, input().split()))
    stk = s_states[t]
    print(stk[k - 1])
