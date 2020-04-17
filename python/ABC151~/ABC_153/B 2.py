

def main():
    H,  _ = map(int, input().split())
    A = list(map(int, input().split()))

    flag = False

    for a in A:
        H -= a
        if H <= 0:
            flag = True
            break
    if flag:print("Yes")
    else: print("No")






if __name__ == "__main__":
    main()