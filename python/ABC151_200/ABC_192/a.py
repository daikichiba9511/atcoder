import sys
def main():
    def input(): return sys.stdin.readline()[:-1]
    x = int(input())
    cnt = 0
    while True:
        x += 1
        cnt += 1
        if x % 100 == 0:
            break
    print(cnt)


if __name__ == "__main__":
    main()