def main():
    a, b = map(int, input().split())
    if b == 1:
        print(0)
    else:
        cnt = 0
        target = a
        while True:
            cnt += 1
            if target >= b:
                break
            target += a -1
        print(cnt)

if __name__ == "__main__":
    main()