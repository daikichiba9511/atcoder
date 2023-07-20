n, k = map(int, input().split())
s = input()
sum_1 = s.count("1")
if abs(k - sum_1) % 2 == 0:
    print("Yes")
else:
    print("No")
