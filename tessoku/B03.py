N = int(input())
A = [int(i) for i in input().split()]

is_equal = False
for i in range(len(A)):
    for j in range(len(A)):
        for k in range(len(A)):
            if i == j or j == k or i == k:
                continue
            s = A[i] + A[j] + A[k]
            if s == 1000:
                is_equal = True
print("Yes" if is_equal else "No")
