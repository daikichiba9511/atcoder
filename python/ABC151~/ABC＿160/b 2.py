def main():
    x = int(input())
    n_hund = x // 500
    n_five = (x - 500 * n_hund) // 5
    print(1000 * n_hund + 5 * n_five)


if __name__ == "__main__":
    main()