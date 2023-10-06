n = int(input())
s = input()

res = False
for i in range(0, n - 3):
    if s[i:i + 3] == 'RRR' or s[i:i + 3] == 'BBB':
        res = True
        break
print("Yes" if res else "No")
