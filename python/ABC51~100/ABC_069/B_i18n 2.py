
def main()->None:
    S:str = input()
    size:int = len(S) - 2
    print("{}{}{}".format(S[0],str(size),S[-1]))

if __name__ == "__main__":
    main()