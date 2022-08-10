N, L, R = map(int, input().split())

# accumns[i] = a[0] + a[1] + ... + a[i-1]
A = list(map(int, input().split()))

accums = [0]
for a in A:
    accums.append(accums[-1] + a)


# left[l] = l * L - accums[l]
left = [l * L - accums[l] for l in range(N + 1)]

# right[r] = (N - r) * R + accums[r]
right = [(N - r) * R + accums[r] for r in range(N + 1)]

# 累積min
rightmin = right
for i in range(N - 1, -1, -1):
    rightmin[i] = min(rightmin[i], rightmin[i + 1])


ans = L * N
for x in range(N + 1):
    tmp = left[x] + rightmin[x]
    ans = min(ans, tmp)

print(ans)
