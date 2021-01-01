
def main():
    _ = int(input())
    a_l = list(map(int, input().split()))
    frac = 0
    for a in a_l:
        frac += (1 / a)
    print(1/frac)
if __name__ == "__main__":
    main()