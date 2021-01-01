def main():
    n = int(input())
    s = input()
    cnt = 0
    for i in range(n-2):
        if s[i]+s[i+1]+s[i+2] == "ABC":
            cnt += 1
    print(cnt)

if __name__ == "__main__":
    main()