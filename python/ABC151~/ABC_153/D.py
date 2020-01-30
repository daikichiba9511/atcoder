
def main():
    import math

    H = int(input())
    if H == 1:
        print(1)
    else:
        count = int(math.log(H, 2))
        ans = 0
        for i in range(count+1):
            ans += 2 ** (i)
        print(ans)

if __name__ == "__main__":
    main()