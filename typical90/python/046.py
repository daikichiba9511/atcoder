n = int(input())
a = list(map(int, input().split()))
b = list(map(int, input().split()))
c = list(map(int, input().split()))

cnt_a = [0] * 46
cnt_b = [0] * 46
cnt_c = [0] * 46
for a_i in a:
    cnt_a[a_i % 46] += 1
for b_i in b:
    cnt_b[b_i % 46] += 1
for c_i in c:
    cnt_c[c_i % 46] += 1

# mod46の世界で考える
cnt = 0
for i in range(46):
    for j in range(46):
        for k in range(46):
            if (i + j + k) % 46 == 0:
                cnt += cnt_a[i] * cnt_b[j] * cnt_c[k]
print(cnt)
