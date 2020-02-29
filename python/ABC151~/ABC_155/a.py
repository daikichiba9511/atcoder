def main():
    a, b, c = map(int, input().split())
    flag = False
    if (a == b and b != c) or (a != b and a == c) or (b == c and a != c):
        flag = True
    if flag: print("Yes")
    else: print("No")

if __name__ == "__main__":
    main()
