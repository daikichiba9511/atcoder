

def main()->None:
    # 解説見た
    # 強さを弱い順に並べて、初めからN番目までは各チームの１番弱い人
    # N番から２N番は各チームで２番目に強い人
    N = int(input()) # team数
    a = list(map(int, input().split()))
    sorted_a = sorted(a)
    
    sum_a = 0 # ２番目の人の和
    range_N = range(N)
    for i in range(N):
        sum_a += sorted_a[3*N - 2*i - 2]
    print(sum_a)


if __name__ == "__main__":
    main()