

def main():
    N = int(input())
    l1 = list(map(int, input().split()))
    l2 = list(map(int, input().split()))
    res = 0
    for i in range(N):
        sum_v = sum(l1[0 : i + 1]) +  sum(l2[i:])
        if sum_v > res:
            res = sum_v
    print(res)
    



if __name__ == "__main__":
    main()