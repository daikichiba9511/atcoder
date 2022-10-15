N = int(input())

for x in range(9, -1, -1):
    divisor = 1 << x
    print((N // divisor) % 2, end="")
print()
