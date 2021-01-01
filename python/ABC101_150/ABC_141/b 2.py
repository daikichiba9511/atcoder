def main():
    s = input()
    flag = False
    for i in s[0:len(s):2]:
        if i not in ["R", "U", "D"]:
            flag = True
    for i in s[1:len(s):2]:
        if i not in ["L", "U", "D"]:
            flag = True
    if flag:print("No")
    else:print("Yes")
         

if __name__ == "__main__":
    main()