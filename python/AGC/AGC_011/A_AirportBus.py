from typing import Iterable, List



def main()->None:
    N, C, K = map(int, input().split())
    range_N: Iterable[int] = range(N)
    T: List[int] = [int(input()) for i in range_N] # バスの出発時刻
    T = sorted(T)
    
    bus: int = 0
    passenger: int = 0
    start: int = 0

    for i in range_N: # 乗客の振り分け
        if passenger == 0:
            start = T[i] + K
            passenger = 1

        elif passenger == C:
            bus += 1
            start = T[i] + K
            passenger = 1

        else:
            if T[i] > start:
                bus += 1
                start = T[i] + K
                passenger = 1

            else:
                passenger += 1
    print(bus+1)


if __name__ == "__main__":
    main()