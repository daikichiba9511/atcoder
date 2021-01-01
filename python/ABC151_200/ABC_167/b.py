def main():
    a, b, c, k = map(int, input().split())
    if a + b >= k:
        if a > k:
            print(k)
        else:print(a)

    else:
        l = k - (a + b)
        print(a - l)
    

if __name__ == "__main__":
    main()