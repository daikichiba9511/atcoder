import math

def main()->None:
    a:int, b:int = map(int, input().split())
    print((a + b + 1) // 2) # 偶数は奇数に、奇数は偶数にして２で割って余り捨てる