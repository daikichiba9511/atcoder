
def main():
    S = input()

    flag = False
    for i in range(2):
        tmp = S[i]
        if tmp != S[i+1]:
            flag = True
    if flag : print("Yes")
    else: print("No")

if __name__ == "__main__":
    main()