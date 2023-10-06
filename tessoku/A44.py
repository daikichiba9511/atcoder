# q <= O(10^5)
n, q = map(int, input().split())

a = list(range(1, n + 1))
state = 0
for _ in range(q):
    query = input().split()
    if query[0] == "1":
        x, y = map(int, query[1:])
        if state % 2 == 1:
            x = n + 1 - x
        a[x - 1] = y
    elif query[0] == "2":
        state += 1
    else:
        x = int(query[-1])
        if state % 2 == 1:
            x = n + 1 - x
        print(a[x - 1])
