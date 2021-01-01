def main():
    a, b, c = map(int, input().split())
    residual = a - b
    res = c - residual
    if res < 0: print(0)
    else: print(res)
if __name__ == "__main__":
    main()