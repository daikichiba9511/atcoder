def isOdd(x : int) -> bool:
    if len(str(x)) % 2 == 1:
        return True
    else: return False

def main(): 
    n = int(input())
    cnt = 0
    for i in range(1, n+1):
        if isOdd(i):
            cnt += 1
    print(cnt)
if __name__ == "__main__":
    main()