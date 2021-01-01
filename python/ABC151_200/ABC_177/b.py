import sys

def main():
    def input():return sys.stdin.readline()[:-1]
    s = input()
    t = input()

    res = len(t)
    # 部分文字列の探索
    for i in range(len(s)-len(t)+1):
        diff = 0
        for j in range(len(t)):
            if s[i + j] != t[j]:
                diff += 1
        res = min(res, diff)
    print(res)
if __name__ == '__main__':
    main()