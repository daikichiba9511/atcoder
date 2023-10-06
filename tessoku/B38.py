n = int(input())
s = input()

# 草0は1かと思ったけど、例の3回目のBで0になるので問題分の草がかならず1以上に反してるので違う
# 最小を目指すので隣り合う草との差分の絶対値は1とおもったけどこれも例の解説から違う
# len(s) = (草の数) - 1 なので、草の数はlen(s) + 1
# 計算量:O(N)
a_ope_mins = [1]
for s_i in s:
    if s_i == 'A':
        a_ope_mins.append(a_ope_mins[-1] + 1)
    else:
        a_ope_mins.append(1)

b_ope_mins = [1]
for s_i in s[::-1]:
    if s_i == 'B':
        b_ope_mins.append(b_ope_mins[-1] + 1)
    else:
        b_ope_mins.append(1)
b_ope_mins = b_ope_mins[::-1]

res = 0
for a_i, b_i in zip(a_ope_mins, b_ope_mins):
    res += max(a_i, b_i)
print(res)
