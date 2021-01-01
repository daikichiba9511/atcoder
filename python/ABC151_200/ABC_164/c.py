def main():
    n = int(input())
    s = [input() for _ in range(n)]
    kind = set(s)
    print(len(kind))

if __name__ == "__main__":
    main()