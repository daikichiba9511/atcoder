def main():
    a, b = map(int, input().split())
    res = [(a+b), (a*b), (a-b)]
    print(max(res))

if __name__ == "__main__":
    main()