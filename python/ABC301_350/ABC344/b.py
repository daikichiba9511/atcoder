a = []
while True:
    ai = int(input())
    a.append(ai)
    if ai == 0:
        break

a.reverse()
for ai in a:
    print(ai)
