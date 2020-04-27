def main():
    n, m = map(int, input().split())
    s, c = []*m, []*m
    for i in range(m):
        a, b = map(int, input().split())
        s.append(a), c.append(b)
    for i in range(0, 10 ** n):
        loop = True
        string = str(i)
        if len(string) != n:
            continue
        for j in range(m):
            if string[s[j] - 1] != str(c[j]):
                loop = False
        if loop:
            print(string)
            quit()
    print(-1)
if __name__ == "__main__":
    main()