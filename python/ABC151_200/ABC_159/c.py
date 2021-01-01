def main():
    l = int(input())
    maxv = 0
    for i in range(1,l):
        for j in range(1, l):
            h = l - i - j
            if h > 0:
                v = i * j * h
                if v > maxv:
                    maxv = v
    print(v)


if __name__ == "__main__":
    main()