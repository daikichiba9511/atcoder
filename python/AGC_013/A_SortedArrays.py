

def main()->None:
    # http://drken1215.hatenablog.com/entry/2019/03/28/014100
    N = int(input())
    A = list(map(int, input().split()))

    res = 0
    i = 0
    while i < N  :
        # sameを抜ける
        while (i+1 < N) and (A[i] == A[i+1]):
            i += 1 
        # up
        if (i+1 < N) and (A[i] < A[i+1]):
            while (i+1 < N) and (A[i] <= A[i+1]):
                i += 1
        # down
        elif (i+1 < N) and A[i] > A[i+1]:
            while (i+1 < N) and (A[i] >= A[i+1]):
                i += 1
        res += 1
        i += 1
    print(res)


if __name__ == "__main__":
    main()