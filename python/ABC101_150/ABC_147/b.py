
def main():
    s = input()
    length = len(s)
    cnt = 0
    for i, j in zip(s[:(length//2)], s[(length//2):][::-1]):
        if i != j:
            cnt += 1
    print(cnt)

if __name__ == "__main__":
    main()