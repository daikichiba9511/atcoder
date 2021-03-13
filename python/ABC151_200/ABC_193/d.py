import sys


def calc_point(x: List[int]) -> int:
    score = 0
    for i in range(1, 10):
        c_i = x.count(i)
        score += i * (10 ** c_i)
    return score

def main():
    def input():
        return sys.stdin.readline()[:-1]
    k = int(input())
    s = input()[:4]
    t = input()[:4]
    

if __name__ == "__main__":
    main()
