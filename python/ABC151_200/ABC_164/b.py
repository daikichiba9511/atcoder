def main():
    a, b, c, d = map(int, input().split())
    flag = False
    while True:
        c -= b
        if c <= 0:
            flag = True
            break
        a -= d
        if a <= 0:
            break
    if flag:print("Yes")
    else:print("No")

if __name__ == "__main__":
    main()