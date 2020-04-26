def main():
    s = input()
    cnt = 0
    for i in range(len(s)-3):
        for j in range(i+3, len(s)+1, ):
            if i == j : continue
            tmp = s[i:j]
            if int(tmp) % 2019 == 0:
                cnt += 1
    print(cnt)
if __name__ == "__main__":
    main()