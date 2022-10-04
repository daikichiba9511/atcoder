import bisect

N = int(input())
A = list(map(int, input().split()))


# 円環は列にして2倍にする
seq = [*A, *A]
accum_seq = [seq[0]]
for i in range(1, len(seq)):
    accum_seq.append(accum_seq[-1] + seq[i])

# O(NlogN)
b_n = accum_seq[N - 1]
if accum_seq[N - 1] % 10 == 0:
    for l in range(N):
        b_l = accum_seq[l]
        b_r = b_l + b_n // 10
        pos = bisect.bisect_left(accum_seq, b_r, lo=l)
        if pos >= len(accum_seq):
            break
        if accum_seq[pos] == b_r:
            print("Yes")
            exit()
    print("No")
else:
    print("No")
