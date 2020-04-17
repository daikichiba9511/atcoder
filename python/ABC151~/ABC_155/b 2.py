def main():
    N = int(input())
    a = list(map(int, input().split()))    
    even_num = [e for e in a if e % 2 == 0]
    flag = True
    for e in even_num:
        if e % 3 != 0 and e % 5 != 0:
            flag = False
    if flag: print("APPROVED")
    else: print("DENIED")
        
if __name__ == "__main__":
    main()