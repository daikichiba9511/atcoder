def main():
    n, k = map(int, input().split())
    h_l = list(map(int, input().split()))
    cnt = 0
    for h_i in h_l:
        if h_i >= k:
            cnt += 1
    print(cnt)

if __name__ == "__main__":
    main()