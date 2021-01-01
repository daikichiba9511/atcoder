
def main()->None:
    alphabet: str = "abcdefghijklmnopqrstuvwxyz"
    S: str = input()
    sorted_s: str = sorted(S)
    flag: bool = False
    for i in alphabet:
        if i not in sorted_s:
            flag = True
            break
    if flag:print(i)
    else:print("None")



if __name__ == "__main__":
    main()