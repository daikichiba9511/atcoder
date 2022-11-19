S = input()

pos = -1
for i, s in enumerate(S):
    if s == "a":
        pos = i + 1

print(pos)
