def main():
    n = int(input())
    s = input()
    alphabet = ["A", "B", "C", "D", "E", "F","G",
                "H", "I", "J", "K", "L", "M", "N",
                "O", "P", "Q", "R", "S", "T", "U",
                "V", "W", "X", "Y", "Z"]
    res = ""
    for i in s:
        idx = alphabet.index(i)
        target_idx = idx + n
        if target_idx > 25:
            target_idx -= 26
        res += alphabet[target_idx]
    print(res)
if __name__ == "__main__":
    main()