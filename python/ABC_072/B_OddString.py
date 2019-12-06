from typing import List
def main()->None:
    s:str = input() # 入力文字列
    counter:int = 0 # 文字のindex,ただし１始まりに注意、pythonは０始まり
    res:List[int] = [] # 条件を満たした文字を一つずつ格納
    for i in s:
        counter += 1
        if counter % 2 != 0:
            res.append(i)

    print("".join(res)) # 最後リスト内にある文字全て連結して出力

if __name__ == "__main__":
    main()