from itertools import combinations

def main():
    n, m = map(int, input().split())
    A = [list(map(int, input().split())) for _ in range(n)]
    res = 0
    for m1, m2 in combinations(range(0,m), 2):
        point_j = 0
        for i in range(n):
            point_j += max(A[i][m1], A[i][m2])
        if point_j > res:
            res = point_j
    print(res)
if __name__ == "__main__":
    main()