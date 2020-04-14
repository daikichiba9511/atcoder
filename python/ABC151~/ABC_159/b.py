def isBatch(s):
    for i in range(len(s)//2):
        if s[i] != s[-i-1]:
            return False
    return True

def main():
    s = input()
    condtion1 = ((len(s) - 1) / 2 ) - 1
    condtion2 = ((len(s) + 3) / 2 ) - 1
    flag = False
    for i, j in [(0, int(condtion1)), (int(condtion2), len(s)-1)]:
        if isBatch(s[i:j+1]):
            flag = True
        else:
            flag = False
    if flag:print("Yes")
    else: print("No")

if __name__ == "__main__":
    main()