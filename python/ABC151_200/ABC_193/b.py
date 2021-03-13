import sys


def main():
    def input():
        return sys.stdin.readline()[:-1]

    n = int(input())
    min_pi = 1e+9 + 1
    for i in range(n):
        a_i, p_i, x_i = tuple(map(int, input().split()))
        machine_now = x_i - a_i
        if machine_now > 0:
            # 買える
            if p_i < min_pi:
                min_pi = p_i
    if min_pi == 1e+9 + 1:
        print(-1)
    else:
        print(min_pi)


if __name__ == "__main__":
    main()
