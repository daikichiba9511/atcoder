

def main():
    N, K = map(int, input().split())
    res = K * (K -1)**(N-1)

    print(res)

if __name__ == "__main__":
    main()