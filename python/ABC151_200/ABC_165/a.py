def main():
    K = int(input())
    a, b = map(int, input().split())
    flag = False
    for i in range(a, b+1):
        if i % K == 0:
            flag = True
    if flag:print("OK")
    else:print("NG")

if __name__ == "__main__":
    main()