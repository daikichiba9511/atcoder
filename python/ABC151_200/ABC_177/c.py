import sys
 
def main():
    def input():return sys.stdin.readline()[:-1]
    N = int(input())
    A = list(map(int, input().split(" ")))
 
    mod = 10**9+7

    S = sum(A)
    S2 = sum(map(lambda x: x**2, A))
    print((S**2-S2) // 2 % mod)
if __name__ == "__main__":
    main()