

def main():
    _, K = map(int, input().split())
    H = list(map(int, input().split()))
    H = sorted(H, reverse=True)
    sum_H = 0
    for h in H:
        if K > 0:
            K -= 1
            continue
        sum_H += h
    print(sum_H)

if __name__ == "__main__":
    main()