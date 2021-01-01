

def main():
    N = int(input())
    S = input()

    l = [0]*N
    r = [0]*N
    for i in range(1, N):
        l[i] = l[i-1] + (S[i-1]=="W")
    for i in range(N-1)[::-1]:
        r[i] = r[i+1] + (S[i+1]=="E")

    
    ans = 10**6
    for a, b, in zip(l, r):
        ans = min(a+b, ans)
    print(ans)
    

if __name__ == "__main__":
    main()