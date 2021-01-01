

def main()->None:
    # gridの処理
    # 近傍の座標をdx=[-1,0,1], dy=[-1,0,1]を用いて
    # (xx, yy) が　xx = x + dx , yy = y + dy　とできる
    # 参考：http://prd-xxx.hateblo.jp/entry/2017/10/19/205331
    # 入力のグリッドから一点ずつ座標指定して選んでその周囲８マスを調べる。
    H, W = map(int, input().split())
    src = [input() for _ in range(H)]
    ans = []
    for row in src:
        ans.append(list(row))


    dxdy = [(-1,-1), (-1, 0), (-1, 1), (0, -1), (0, 1), (1, -1), (1, 0), (1, 1)]
    for y in range(H):
        for x in range(W):
            if src[y][x] == "#":continue
            c = 0
            for dx, dy in dxdy:
                # 探索範囲はx:0~W, y:0~Hでその周囲８マスを探索する
                if x+dx < 0 or x+dx > W-1 or y+dy < 0 or y+dy > H-1: continue
                if src[y+dy][x+dx] == "#": c += 1
            ans[y][x] = c
    
    for row in ans:
        print("".join(list(map(str, row))))




if __name__ == "__main__":
    main()