from itertools import permutations, combinations

def main():
    n = int(input())
    x_l = [] ; y_l = []
    for _ in range(n):
        tmp_x, tmp_y = map(int, input().split())
        x_l.append(tmp_x) ; y_l.append(tmp_y)
    cnt = 0
    total_dist = 0
    for c in permutations(range(n)):
        # c の中から２辺の数繰り返す
        for i in range(n-1):
            dist = ((x_l[c[i]] - x_l[c[i+1]])**2 + (y_l[c[i]] - y_l[c[i+1]])**2)**(1/2)
            total_dist += dist
        cnt += 1

    print(total_dist/cnt)

if __name__ == "__main__":
    main()