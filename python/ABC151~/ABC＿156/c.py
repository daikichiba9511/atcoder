

def main():
    n = int(input())
    x = list(map(int, input().split()))

    mu = round((sum(x)/len(x)))
    res = 0
    for i in x:
        res += (i - mu)**2

    print(int(res))

if __name__ == "__main__":
    main()