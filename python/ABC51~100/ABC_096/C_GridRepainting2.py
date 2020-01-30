
def main()->None:
    H, W = map(int, input().split())
    range_H = range(H)
    range_W = range(W)
    src = [input() for _ in range_H]
    #print(src)
    ans = [["." for _ in range_W] for _ in range_H]
    # 周囲4マスの探索するときの配列の場所指定の配列
    dxdy = [(-1,0),(0,-1),(0,1),(1,0)]
    # x, yで配列の位置を指定
    for y in range_H:
        for x in range_W:
            c = "."
            if src[y][x] == ".":continue
            for dx, dy in dxdy: # 周囲８マスを探索
                if x+dx < 0 or x+dx > W-1 or y+dy < 0 or y+dy > H-1 :continue
                if src[y+dy][x+dx] == "#": #周囲に黒マスがあれば対象の黒マスは黒くしていい
                    c = "#"
            ans[y][x] = c
    #print(ans)
    flag = True
    counter = 0
    for i in ans:
        res = "".join(i)
        if res == src[counter]:
            counter += 1
        else:
            flag = False
    if flag: print("Yes")
    else: print("No")



if __name__ == "__main__":
    main()