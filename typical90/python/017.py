class BIT:
    def __init__(self, size: int) -> None:
        self._size = size + 2
        self._bit = [0] * (size + 2)

    def add(self, pos: int, x: int) -> None:
        pos += 1
        while pos <= self._size:
            self._bit[pos] += x
            pos -= pos & -pos

    def sum(self, pos: int) -> int:
        s = 0
        pos += 1
        while pos >= 1:
            s += self._bit[pos]
            pos -= pos & -pos
        return s


def main():
    N, M = map(int, input().split())
    L = []
    R = []
    for _ in range(M):
        l, r = map(int, input().split())
        L.append(l)
        R.append(r)

    # pattern1
    ans1 = 0

    a = [
        111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111
    ]


if __name__ == "__main__":
    main()
