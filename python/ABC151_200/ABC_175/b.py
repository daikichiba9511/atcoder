from itertools import combinations


def valid_tri(l)->bool:
    if l[0] != l[1] and l[1] != l[2] and l[0] != l[2]:
        # print(l)
        if l[0] + l[1] > l[2] and l[1] + l[2] > l[0] and l[0] + l[2] > l[1]:
            return True
        else: return False
    else: return False

def main():
    n = int(input())
    l = list(map(int, input().split()))
    cnt = 0
    for l in combinations(l, 3):
        if valid_tri(l):
            cnt += 1

    print(cnt)

if __name__ == "__main__":
    main()