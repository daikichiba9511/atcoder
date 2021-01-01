from itertools import permutations
import numpy as np

def main():
    n = int(input())
    p = list(map(int, input().split()))
    q = list(map(int, input().split()))

    cnt = 0
    a = 0
    b = 0
    for i in permutations(range(1,n+1)):
        cnt += 1
        if list(i) == p :
            a = cnt
        if list(i) == q :
            b = cnt

    print(np.abs(a-b))

if __name__ == "__main__":
    main()