# 全探索だと間に合わない？

def main():
    N = input()
    res = 0
    for i in N:
        res += int(i)

    if res % 9 == 0:
        print("Yes")
    else: print("No")

if __name__ == "__main__":
    main()