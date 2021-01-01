def main():
    s = input()
    t = input()

    alphabet = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"]

    for i in alphabet:
        if s + i == t:
            print("Yes")
            quit(0)
    print("No")



if __name__ == "__main__":
    main()