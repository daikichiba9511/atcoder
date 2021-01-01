# https://atcoder.jp/contests/abc106/tasks/abc106_b

def main():
    n = int(input())

    # 奇数の数列生成
    odd = [i for i in range(1, n+1, 2)]

    res = 0
    for i in odd:
        cnt = 0
        for j in range(1, i+1, 2):
            if i % j == 0:
                cnt += 1
        if cnt == 8:
            res += 1
    print(res)
if __name__ == "__main__":
    main()