# 回答見た
def main()->None:
    s:int = input()
    print(s.rfind("Z") - s.find("A") + 1)

if __name__ == "__main__":
    main()