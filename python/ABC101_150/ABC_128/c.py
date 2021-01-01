# & を勘違いしていてできていなかった。bit & 演算子は同じ位置のbitが１の時１を返す
# 1 << n は１を左にｎこシフトさせるから2**n と等しい。例えばn=3の時　1<<3=1000 => この２進数を
# 10進数に直すと8 = 2 ** 3


def main():
    n, m = map(int, input().split())
    # ｋは何個のスイッチにつながっているか、ｓはスイッチの番号
    s = []; k = [] # s : どのスイッチとつながってるか、インデックスは電球を指す、　k: 電球が何個のスイッチとつながっているか
    for _ in range(m):
        tmp = list(map(int, input().split()))
        s.append(tmp[1:]); k.append(tmp[0])
    p = list(map(int, input().split()))

    res = 0
    # スイッチの状態は２進数表記で表す。スイッチはｎ個あるので
    for bit in range(2**n):
        ok = True
        for i in range(m): # 各電球に対して見ていく
            cnt = 0
            for v in s[i]: # 各電球につながっているスイッチを見てる
                if ( bit & 1 << (v - 1) ): # bitの状態がスイッチvがついてる状態なのかどうか
                    cnt += 1
            if cnt % 2 != p[i]:
                ok = False
        if ok: # okなら全ての電球が付いているということ
            res += 1

    print(res)

if __name__ == "__main__":
    main()