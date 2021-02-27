import sys


def main():
    def input(): return sys.stdin.readline()[:-1]
    S = input()
    flag = True
    for idx in range(len(S)):
        if idx % 2 == 0:
            if str.islower(S[idx]):
                continue
            else:
                flag = False
                break
        else:
            if str.isupper(S[idx]):
                continue
            else:
                flag = False
                break
    if flag: print("Yes")
    else: print("No")

if __name__ == "__main__":
    main()
