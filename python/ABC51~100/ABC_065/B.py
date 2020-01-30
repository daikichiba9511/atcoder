

def main():
    N = int(input())
    a = [int(input()) for _ in range(N)]
    
    b = a[0]
    count = 1
    if b == 2:
        ans = 1
    else:
        while True:
            count += 1
            b = a[b - 1]
            if b == 2:
                ans = count
                break
        
            if count > N:
                ans = -1
                break
    print(ans)

if __name__ == "__main__":
    main()