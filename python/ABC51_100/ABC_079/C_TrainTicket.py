

def main():
    s = input()
    for i in range(2 ** (len(s)-1)):
        total = int(s[0])
        ope = s[0]
        for j in range(len(s)-1):
            if ((i >> j) & 1):
                total += int(s[1+j])
                ope = ope + "+" + s[1+j]
            else:
                total -= int(s[1+j])
                ope = ope + "-" + s[1+j]
        if total == 7:
            print(ope+"=7")
            break

if __name__ == "__main__":
    main()