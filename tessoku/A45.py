n, c = input().split()
n = int(n)
a = input()

score = 0
for i in range(n):
    a_i = a[i]
    if a_i == "R":
        score += 2
    elif a_i == "B":
        score += 1

c_score = {"R": 2, "B": 1, "W": 0}[c]
print("Yes" if score % 3 == c_score else "No")
