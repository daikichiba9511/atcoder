def main():
    x = int(input())
    cnt = 0
    money = 100
    while True:
        money = int(1.01 * money)
        cnt += 1
        if money >= x:
            break
    print(cnt)

if __name__ == "__main__":
    main()