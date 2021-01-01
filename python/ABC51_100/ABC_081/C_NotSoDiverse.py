from collections import Counter
from typing import List

def main()->None:
    # 実行時間が間に合わず回答見た
    # このcounter がめちゃ便利。pythonって感じがする
    n, k = map(int, input().split())
    a: List[int] = list(map(int, input().split()))
    a = sorted(Counter(a).values(), reverse=True)
    print(sum(a[k:]))

if __name__ == "__main__":
    main()