from typing import List
# 回答見た
def main()->None:
    N:int = int(input())
    T:int, A:int = map(int, input().split())
    H:List[int] = [int(i) for i in input().split()]
    diff:List[int] = [abs(A-(T-0.006*i)) for i in H]
    print(diff.index(min(diff))+1)


if __name__ == "__main__":
    main()

