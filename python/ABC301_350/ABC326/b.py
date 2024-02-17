n = int(input())

for n in range(n, 920):
    n100 = n // 100
    n10 = (n - n100 * 100) // 10
    n1 = n - n100 * 100 - n10 * 10
    if n100 * n10 == n1:
        print(n)
        break
