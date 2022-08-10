cards = tuple(map(int, input().split()))

cnt = [0] * 14
for card in cards:
    cnt[card] += 1

flag2 = False
flag3 = False
for c in cnt:
    if c == 3:
        flag3 = True
    if c == 2:
        flag2 = True

if flag2 and flag3:
    print("Yes")
else:
    print("No")
