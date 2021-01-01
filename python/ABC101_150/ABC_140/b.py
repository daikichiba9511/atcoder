def main():
    _ = int(input())
    a_l = list(map(int, input().split()))
    b_l = list(map(int, input().split()))
    c_l = list(map(int, input().split()))
    res = 0
    pre = 0
    for a in a_l:
        res += b_l[a-1]
        if (a - pre == 1) and (a != 1):
            res += c_l[a-2]
        pre = a
    print(res)

if __name__ == "__main__":
    main()