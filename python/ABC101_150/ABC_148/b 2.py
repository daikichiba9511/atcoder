def main():
    n = int(input())
    s, t = input().split()
    res = ""
    for i in range(n):
        res += s[i]+t[i]
    print(res)


if __name__ == "__main__":
    main()