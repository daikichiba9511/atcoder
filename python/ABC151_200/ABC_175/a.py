def main():
    s = input()
    if s == "RSR":
        print(1)
    else:
        cnt = 0
        for i in s:
            if i == "R":
                cnt += 1

        print(cnt)

if __name__ == "__main__":
    main()
