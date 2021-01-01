


def main()->None:
    S:str = input()

    counter:int = 0
    if S[0] == "o":counter +=1
    if S[1] == "o":counter +=1
    if S[2] == "o":counter +=1
    print(700+100*counter)


if __name__ == "__main__":
    main()