s = input()
bar_i = []
for i in range(len(s)):
    if s[i] == "|":
        bar_i.append(i)
print(s[: bar_i[0]] + s[bar_i[1] + 1 :])
