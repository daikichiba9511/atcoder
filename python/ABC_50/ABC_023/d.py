# 完全に理解してる訳じゃない

# 割られた時の風船の高度は全てmid以下か判定
def isPossible(n, H, S, mid):
    count = [0]*n # 高さｘに到達するまでの時間
    for i in range(n):
        if H[i] > mid: # mid = x : 割られた時の風船の高度は全てmid以下
            return False
        else:
            # (mid - x[i]) / S[i] は風船iを割ることができる時間
            count[min(n-1, int((mid-H[i]) / S[i]))] += 1
    # 風船がｊ＋１秒以内であることを確認
    # j秒以内に割り切れることができる
    for j in range(n-1): # 時間の累積和
        count[j+1] += count[j]
    for j in range(n):
        if count[j] > j+1:
            return False
    return True

def main():
    # 入力
    n = int(input())
    s_l = [0]*n; h_l = [0]*n
    for i in range(n):
        tmp_h, tmp_s = map(int, input().split())
        s_l[i] = tmp_s; h_l[i] = tmp_h

    # 二分探索
    left = -1 # idx = 0が条件を満たすこともあるの初期値-1
    right = 1e+18
    while right - left > 1: # 左がFalse、右がTrueのギリギリまで
        mid = int((right + left )/ 2)
        if isPossible(n, h_l, s_l, mid):
            right = mid
        else:
            left = mid
    print(right)

if __name__ == "__main__":
    main()