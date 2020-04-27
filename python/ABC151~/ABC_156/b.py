


def main():
    def digit(x, n):
        x_tmp = x
        res = ''
        while x_tmp > 0:
            res += str(x_tmp % n)
            x_tmp = int(x_tmp/n)
        return len(res)

    n, k = map(int, input().split())

    print(digit(n, k))



if __name__ == "__main__":
    main()