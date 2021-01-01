

def main()->None:
    N: int = int(input())
    A: int = map(int, input().split())

    odd_count: int = 0
    for a in A:
        if a % 2 == 1:
            odd_count += 1

    if odd_count % 2 == 0:
        print("YES")
    else:
        print("NO")



if __name__ == "__main__":
    main()