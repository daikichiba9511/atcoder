N = int(input())

A1 = N // 3
A2 = N // 5
A3 = N // 7
A4 = N // 15
A5 = N // 21
A6 = N // 35
A7 = N // 105

print(A1 + A2 + A3 - A4 - A5 - A6 + A7)
