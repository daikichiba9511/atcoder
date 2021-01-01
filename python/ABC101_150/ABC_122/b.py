# https://atcoder.jp/contests/abc122/tasks/abc122_b

def main():
    s = input()
    res = 0
    for i in range(len(s)):
        for j in range(i, len(s)):
            if all("ACGT".count(c) == 1 for c in s[i:j+1]):
                res = max(res, j-i+1)
    print(res)

if __name__ == "__main__":
    main()