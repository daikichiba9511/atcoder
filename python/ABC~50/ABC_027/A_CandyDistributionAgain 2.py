from typing import Tuple, List

def main()->None:
    # ヒント見たけど参考にしてない
    N, x = map(int, input().split())
    a:List[int] = list(map(int, input().split()))
    sorted_a:List[int] = sorted(a) # 小さい順にならべる
    count:int = 0 # 何回配ったか
    for d in sorted_a:
        x -= d
        if x < 0: # 持ってた量が配る総量より少なかった時
            break
        count += 1
    # ちょうど配れない、必要な量より多く持ってた時はおおもらう人が出てくる。
    # 幸福人数の最大を求めればいいから余りを全部一人にあげればいいから−１
    if x > 0:
        print(count-1)
    else: # ちょうどの時はcount=N,持ってた量が配る総量より少なかった時は配れた人数
        print(count)

if __name__ == "__main__":
    main()