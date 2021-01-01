def main():
    a = [list(map(int, input().split())) for _ in range(3)]
    n = int(input())
    b = [int(input()) for _ in range(n)]
    card = [[False]*3 for _ in range(3)]
    for i in range(3):
        for j in range(3):
            if a[i][j] in b:
                card[i][j] = True

    ans = "No"
    for i in range(3): #横に見てる
        if card[i][0] and card[i][1] and card[i][2]:
            ans = "Yes"
    for i in range(3): # 縦に見てる
        if card[0][i] and card[1][i] and card[2][i]:
            ans = "Yes"
    if card[0][0] and card[1][1] and card[2][2]:
        ans = "Yes"
    if card[0][2] and card[1][1] and card[2][0]:
        ans = "Yes"
    print(ans)

    
if __name__ == "__main__":
    main()