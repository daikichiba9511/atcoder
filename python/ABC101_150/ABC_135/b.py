def main():
    n = int(input())
    p_l = list(map(int, input().split()))
    cnt = 0
    for i in range(n):
        if p_l[i] == i + 1: continue
        else: cnt += 1
    if cnt > 2: print("NO")
    else: print("YES")
if __name__ == "__main__":
    main()