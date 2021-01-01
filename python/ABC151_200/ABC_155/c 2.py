def main():
    n = int(input())
    s = [input() for i in range(n)]
    res = {}
    for i in s:
        if i not in res:
            res[i] = 1
        res[i] += 1
    keys = max(res.values())
    max_keys = sorted([key for key in res if res[key] == keys])
    for k in max_keys:
        print(k)

if __name__ == "__main__":
    main()