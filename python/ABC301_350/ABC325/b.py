n = int(input())

wx = []
for _ in range(n):
    wx.append(tuple(map(int, input().split())))


ans = 0
for i in range(0, 25):
    tmp_w_sum = 0
    for w, x in wx:
        if 9 <= (i + x) % 24 <= 18 and 9 <= (i + 1 + x) % 24 <= 18:
            tmp_w_sum += w
    ans = max(ans, tmp_w_sum)
print(ans)

